import { Accessor, Setter, batch, createMemo, createSignal } from "solid-js";
import { SetStoreFunction, createStore, produce } from "solid-js/store";
import * as Mech from "./types/mech";
import { create_ws } from "./ws";

//------------------------------------------------------------------------------
// Utils
//------------------------------------------------------------------------------

export function get_in(root: Span, path: number[]) {
    let cur: Subject|undefined = root;
    for(let ix of path) {
        cur = cur?.events?.[ix];
    }
    return cur;
}

export interface Placeholder {
    "event": "placeholder",
    selection_path: number[],
    span_type?: undefined,
    events?: undefined
}

export type Subject = Message.Event|Span|Placeholder;


//------------------------------------------------------------------------------
// Messages
//------------------------------------------------------------------------------

export namespace Message {
    export interface Base {
        event: string,
        span?: string[],
        selection_path: number[],
        span_type?: undefined,
        events?: undefined,
        [key: string]: unknown
    }

    export interface SpanStart extends Base {
        event: "span_start",
        span: string[],
        start_time: number,
    }
    export interface SpanEnd extends Base {
        event: "span_end",
        span: string[],
        start_time: number,
        end_time: number,
        elapsed: number,
    }

    export interface Time extends Base {
        event: "time",
        type: string,
        elapsed: number,
        results?: ResultData
    }
    export function is_time(span: any): span is Message.Time {
        return span?.event === "time";
    }

    export interface Error extends Base {
        event: "error",
        err: any
    }
    export function is_error(span: any): span is Message.Error {
        return span?.event === "error";
    }

    export interface Compilation extends Base {
        event: "compilation",
        source: Source,
        passes: Pass[],
        emitted: string,
        emit_time: number,
        mech?: Mech.Machine
    }
    export function is_compilation(span: any): span is Message.Compilation {
        return span?.event === "compilation";
    }

    export type Event = Time | Error | Compilation;

    export interface Pass {
        name: string,
        task: string,
        elapsed: number
    }

    export interface Source {
        file: string,
        line: number,
        block: string,
    }

    export interface ResultData {
        values: Record<string, any>[],
        count: number
    }
}
export type Message =
    | Message.SpanStart
    | Message.SpanEnd
    | Message.Event

//------------------------------------------------------------------------------
// Spans
//------------------------------------------------------------------------------

export namespace Span {
    export interface Base {
        event: "span",
        span_type: string,
        span: string[];
        start_time: number,
        end_time?: number,
        elapsed?: number,
        selection_path: number[],

        events: (Span | Message.Event)[],

        last_dirty_clock?: number,
        [key: string]: unknown,
    }

    export function is_span(span: any): span is Span {
        return span?.event === "span" && Array.isArray(span.events);
    }

    export interface Program extends Base {
        span_type: "program",
        main: string,
        run: number,
    }

    export function is_program(span: any): span is Program {
        return is_span(span) && span.span_type === "program";
    }

    export interface Block extends Base {
        span_type: "rule"|"query",
        task: string,
        mech: Mech.Machine
    }

    export function is_block(span: any): span is Block {
        return is_span(span) && (span.span_type === "rule" || span.span_type === "query"); //  && span?.name !== "pyrel_base"
    }

    export interface Rule extends Block {
        span_type: "rule"
    }

    export function is_rule(span: any): span is Rule {
        return is_span(span) && span.span_type === "rule";
    }

    export interface Query extends Block {
        span_type: "query",
        results?: Message.ResultData,
        errors?: any
    }

    export function is_query(span: Span|Message.Event): span is Query {
        return is_span(span) && span.span_type === "query";
    }
}
export type Span =
    | Span.Query
    | Span.Rule
    | Span.Base;

//------------------------------------------------------------------------------
// Client
//------------------------------------------------------------------------------

export class DebuggerClient {
    connection: Connection;
    messages: Accessor<Message[]>;
    protected set_messages: Setter<Message[]>;


    run_counter = 0;
    root: Span;
    protected set_root: SetStoreFunction<Span>;

    spans() {
        return this.root.events;
    }

    connected: Accessor<boolean>;
    protected set_connected: Setter<boolean>;

    protected path: number[] = [];

    latest: Accessor<Span.Program|undefined>;
    latest_blocks: Accessor<Span.Block[]|undefined>;

    constructor(ws_url: string) {
        this.connection = new Connection(ws_url);
        [this.messages, this.set_messages] = createSignal<Message[]>([], {equals: () => false});
        [this.root, this.set_root] = createStore<Span>({
            event: "span",
            span_type: "root",
            span: [],
            start_time: 0,
            events: [],
            selection_path: []
        });
        [this.connected, this.set_connected] = createSignal<boolean>(false, {equals: () => false});

        this.latest = createMemo(() => {
            return this.spans().findLast(Span.is_program);
        }, undefined, { equals: (prev, neue) => false });

        this.latest_blocks = createMemo(() => {
            return this.latest()?.events.filter(Span.is_block) ?? [];
        }, [], { equals: () => false });

        this.connection.onreceive = this.handle_message;
        this.connection.onconnect = this.set_connected;
    }

    clear() {
        batch(() => {
            this.path = [];
            this.set_messages([]);
            this.set_root({event: "span", span_type: "root", span: [], start_time: 0, events: []});
        });
    }

    protected handle_span_start(msg: Message.SpanStart) {
        this.set_root(produce((root) => {
            let parent = get_in(root, this.path);
            if(!parent || !Span.is_span(parent)) throw new Error();
            this.path.push(parent.events.length);
            let span_type = msg.span[msg.span.length - 1];
            let sub: Span = {
                ...msg,
                span_type,
                event: "span",
                selection_path: this.path.slice(),
                run: span_type === "program" ? ++this.run_counter : undefined,
                events: []
            };
            parent.events.push(sub)
        }));
    }

    protected handle_span_end(msg: Message.SpanEnd) {
        this.set_root(produce((root) => {
            let start = get_in(root, this.path);
            if(!start || !Span.is_span(start)) throw new Error();
            for (let key in msg) {
                if (key === "span" || key === "event") continue;
                start[key] = msg[key];
            }
            this.path.pop();
        }));
    }

    protected handle_event(msg: Message.Event) {
        this.set_root(produce((root) => {
            let span = get_in(root, this.path);
            if(!span || !Span.is_span(span)) throw new Error();
            msg.selection_path = [...this.path, span.events.length],
            span.events.push(msg);
        }));
    }

    protected handle_message = (msg: Message) => {
        batch(() => {
            if(msg.event === "span_start") this.handle_span_start(msg)
            else if(msg.event === "span_end") this.handle_span_end(msg)
            else this.handle_event(msg);

            this.set_messages((prev) => {
                prev.push(msg);
                return prev;
            });
        });
    }
}

//------------------------------------------------------------------------------
// Connection
//------------------------------------------------------------------------------

export class Connection {
    private socket: WebSocket | null = null;
    private shouldReconnect = true;
    private active = false;

    ws_url: string;
    reconnectInterval: number;
    onreceive?: (msg: any) => void;
    onconnect?: (is_connected: boolean) => void;

    constructor(ws_url: string, reconnectInterval: number = 1_000) {
        this.ws_url = ws_url;
        this.reconnectInterval = reconnectInterval;
        this.connect();
    }

    private connect(): void {
        // @NOTE: I wasted an hour trying to figure out how to suppress the default error message and then gave up.
        this.socket = create_ws(this.ws_url);

        this.socket.addEventListener("open", () => {
            this.active = true;
            this.onconnect?.(true);
        });

        this.socket.addEventListener("message", (event) => {
            let msg;
            try {
                msg = JSON.parse(event.data);
            } catch (err: any) {
                console.warn("Failed to parse message:", event.data);
            }
            if(msg.event === "span_end" && msg.span?.length === 1 && msg.span[0] === "program") {
                this.active = false;
            }
            this.onreceive?.(msg);
        });

        this.socket.addEventListener("close", () => {
            this.onconnect?.(false);
            if(this.active) {
                console.warn("Disconnected unexpectedly from the WebSocket server");
                this.active = false;
            }

            if (this.shouldReconnect) {
                setTimeout(() => this.connect(), this.reconnectInterval);
            }
        });

        this.socket.addEventListener("error", (event) => {
            if (this.socket) {
                this.socket.close();
            }
        });
    }

    public send(msg: string|ArrayBufferLike|Blob|ArrayBufferView) {
        if(this.active) {
            this.socket?.send(msg);
        }
    }

    public disconnect() {
        if (this.socket) {
            this.socket.close();
        }
    }

    public close(): void {
        this.shouldReconnect = false;
        this.disconnect();
    }
}

export const client = new DebuggerClient(`ws://${location.hostname}:5678`);
