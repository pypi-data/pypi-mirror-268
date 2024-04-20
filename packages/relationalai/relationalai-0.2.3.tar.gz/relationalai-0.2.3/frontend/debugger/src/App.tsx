import { Show, createEffect, createSignal } from "solid-js";
import { EventListSelection, Selection } from "./Selection";
import { EventList } from "./components/EventList";
import { EventViewer } from "./components/EventViewer";
import { Sidebar } from "./components/Sidebar";
import { Button } from "./components/ui/Button";
import { Field, Format } from "./components/ui/Field";
import { Icon } from "./components/ui/Icon";
import { Modal } from "./components/ui/Modal";
import { Tooltip } from "./components/ui/Tooltip";
import { client, get_in, type Subject } from "./debugger_client";
import "./App.styl";

function App() {
    const event_list_selection = new Selection<Subject>("EventList");

    const clear = () => {
        client.connection.disconnect();
        event_list_selection.clear()
        client.clear();
    };

    const [pinned, set_pinned] = createSignal<boolean>(true);

    createEffect((prev_len: number|undefined) => {
        const cur_len = client.spans().length;
        const cur = event_list_selection.primary();
        if (pinned() && cur_len !== prev_len && cur) {
            event_list_selection.select({ event: "placeholder", selection_path: [cur_len - 1, ...cur.selection_path.slice(1)] })
        }
        return cur_len;
    });

    createEffect(() => {
        let selected = event_list_selection.primary();
        if (selected?.event === "placeholder") {
            let available = get_in(client.root, selected.selection_path);
            if(available) {
                event_list_selection.select(available);
            }
        }
    });

    return (
        <EventListSelection.Provider value={event_list_selection}>
            <app-chrome>
                <Sidebar side="left" defaultOpen>
                    <header>
                        <Button class="icon" onclick={clear} tooltip="clear events">
                            <Icon name="ban" />
                        </Button>
                        <Button class="icon" tooltip="Follow last run" onclick={() => set_pinned(v => !v)}>
                            <Icon name="pin" type={pinned() ? "filled" : "outline"} />
                        </Button>
                        <span style="flex: 1" />
                        <Modal title="Settings" content={<Settings />}>
                            <Modal.Trigger as={Button} class="icon" tooltip="settings">
                                <Icon name="settings" />
                            </Modal.Trigger>
                        </Modal>
                    </header>
                    <EventList events={client.spans()} />
                </Sidebar>
                <main>
                    <Show when={event_list_selection.primary()}>
                        <EventViewer subject={event_list_selection.primary()!} />
                    </Show>
                    <Show when={event_list_selection.primary()?.event === "placeholder"}>
                        <app-scroller>

                        </app-scroller>
                    </Show>
                </main>
                <Status />
            </app-chrome>
        </EventListSelection.Provider>
    );
};

export default App;

function Status() {
    return (
        <Tooltip content={client.connected() ? "Connected to program" : "Disconnected from program"}>
            <Tooltip.Trigger as="status-icon">
                <Show when={client.connected()} fallback={<Icon name="antenna-bars-off" />}>
                    <Icon name="antenna-bars-5" />
                </Show>
            </Tooltip.Trigger>
        </Tooltip>
    )
}


export function Settings() {
    return (
        <>
            <section>
                <h3>Connection</h3>
                <Field.Number label="Polling Interval" formatOptions={Format.seconds} minValue={1}
                    defaultValue={client.connection.reconnectInterval / 1000}
                    onRawValueChange={(v) => client.connection.reconnectInterval = v * 1000} />
                <Field.Text label={"Debug URL"} placeholder={"ws://localhost:1234"}
                    defaultValue={client.connection.ws_url} onChange={(v) => client.connection.ws_url = v} />
            </section>

        </>
    )
}
