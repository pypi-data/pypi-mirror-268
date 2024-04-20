import { Message, Span, client, type Subject } from "@src/debugger_client"
import { Component, For, Show, useContext, type JSXElement } from "solid-js"
import { Collapsible } from "./ui/Collapsible";
import { EventListSelection } from "@src/Selection";
import { Dynamic } from "solid-js/web";
import { CodeBlock } from "./ui/Code";
import "./EventList.styl";
import { fmt, prefix_of } from "@src/util";
import { Icon } from "./ui/Icon";

//------------------------------------------------------------------------------
// EventList
//------------------------------------------------------------------------------

export interface EventListProps {
    events: (Message.Event | Span)[],
    sub?: boolean
}
export function EventList(props: EventListProps) {
    return (
        <div class={`event-list ${props.sub ? "sub" : ""}`}>
            <For each={props.events}>
                {(event) => <EventListItem event={event} />}
            </For>
        </div>
    )
}

export function EventListItem(props: EventListItemProps) {
    const component = (() => {
        const event = props.event;
        if (Span.is_program(event)) return EventItemProgram;
        if (Span.is_block(event)) return EventItemBlock;
        else if (Span.is_span(event)) return EventItemUnknownSpan;
        else if (Message.is_compilation(event)) return EventItemCompilation;
        else if (Message.is_time(event)) return EventItemTime;
        else return EventItemUnknown;

    }) as () => Component<EventListItemProps>;

    return (
        <Dynamic component={component()} event={props.event} onclick={props.onclick} />
    )
}

//------------------------------------------------------------------------------
// Base components for event list items
//------------------------------------------------------------------------------

export interface EventListItemProps<T extends Subject = Subject> {
    event: T,
    onclick?: (event: Subject) => any
}

interface EventListBranchProps<T extends Span = Span> extends EventListItemProps<T> {
    class?: string;
    children?: JSXElement;
    open?: boolean;
}
export function EventListBranch<T extends Span>(props: EventListBranchProps<T>) {
    const klass = () => `event-list-item branch ${props.event.event} ${props.event.span_type || ""} ${props.class || ""}`;
    return (
        <Collapsible side="top" defaultOpen={props.open} class={klass()}>
            <Collapsible.Trigger as="header">
                <Collapsible.TriggerIcon />
                {props.children}
            </Collapsible.Trigger>
            <Collapsible.Content>
                <EventList sub events={props.event.events} />
            </Collapsible.Content>
        </Collapsible>
    );
}

interface EventListLeafProps<T extends Subject = Subject> extends EventListItemProps<T> {
    class?: string;
    children?: JSXElement;
}
export function EventListLeaf(props: EventListLeafProps<Subject>) {
    const selection = useContext(EventListSelection);
    const klass = () => `event-list-item leaf ${props.event.event} ${props.event.span_type || ""} ${props.class || ""}`;
    const onclick = () => {
        if(props.onclick) props.onclick(props.event);
        else selection?.select?.(props.event);
    }
    return (
        <div class={klass()} onclick={onclick}>
            {props.children}
        </div>
    );
}

//------------------------------------------------------------------------------
// Items
//------------------------------------------------------------------------------

export function EventItemProgram(props: EventListItemProps<Span.Program>) {
    const selection = useContext(EventListSelection);
    const is_selection_inside = () => !!selection.selected().find(item => prefix_of(item.selection_path, props.event.selection_path));
    const should_open = () => is_selection_inside() || client.latest() === props.event;
    return (
        <EventListBranch event={props.event} open={should_open()} class="naked">
            <span class="event-label">Run #{(props.event as Span.Program).run}</span>

            <span class="event-detail">
                {props.event.main}
            </span>
            <span style="flex: 1" />
            <span>
                <Show when={props.event.elapsed} fallback={<Icon name="clock-play" />}>
                    {fmt.time.s(props.event.elapsed!)}
                </Show>
            </span>
        </EventListBranch>
    )
}

export function EventItemBlock(props: EventListItemProps<Span.Block>) {
    const selection = useContext(EventListSelection);
    return (
        <For each={props.event.events}>
            {(event) => <EventListItem event={event} onclick={() => selection?.select(props.event)} />}
        </For>
    )
}


export function EventItemCompilation(props: EventListItemProps<Message.Compilation>) {
    let source = () => props.event?.source;

    return (
        <Show when={source()?.block}>
            <EventListLeaf event={props.event} class="block naked" onclick={props.onclick}>
                <header>
                    <span style="flex: 1" />
                    <span class="event-detail">
                        <span class="file">{source()?.file}:</span>
                        <span class="line">{source()?.line}</span>
                    </span>
                </header>
                <CodeBlock lang="python" dense no_copy>
                    {source()?.block}
                </CodeBlock>
            </EventListLeaf>
        </Show>
    )
}

export function EventItemTime(props: EventListItemProps<Message.Time>) {
    return (
        <EventListLeaf event={props.event} onclick={props.onclick}>
            <span class="event-label">
                {props.event.type}
            </span>
            <span style="flex: 1" />
            <span class="event-detail">
                {fmt.time.ms(props.event.elapsed * 1000)}
            </span>
        </EventListLeaf>
    )
}

export function EventItemUnknownSpan(props: EventListItemProps<Span>) {
    return (
        <For each={props.event.events}>
            {(event) => <EventListItem event={event} onclick={props.onclick} />}
        </For>
    )

    // return (
    //     <EventListBranch event={props.event} class="unknown naked" open>
    //         <span>
    //             {props.event.span_type}
    //         </span>
    //     </EventListBranch>
    // )
}

export function EventItemUnknown(props: EventListItemProps<Message.Event>) {
    return (
        <EventListLeaf event={props.event} class="unknown" onclick={props.onclick}>
            <span>
                {props.event.event}
            </span>
            <span>
                {Message.is_time(props.event) ? props.event.type : undefined}
            </span>
        </EventListLeaf>
    )
}


