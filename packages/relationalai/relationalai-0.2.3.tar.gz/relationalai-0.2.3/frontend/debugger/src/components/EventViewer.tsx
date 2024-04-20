import { Dynamic } from "solid-js/web";
import { Machine } from "./Schematic";
import { Message, Placeholder, Span, Subject } from "../debugger_client";
import "./EventViewer.styl";
import { For, JSXElement, Show } from "solid-js";
import { CodeBlock } from "./ui/Code";

export interface BlockViewerProps {
    subject: Span.Block;
    children?: JSXElement
}
export function BlockViewer(props: BlockViewerProps) {
    const compilation = () => props.subject.events.find(Message.is_compilation)
    return (
        <span-viewer class={`block ${props.subject.span_type}`}>
            <scroll-container>
                <scroll-inner>
                    <section class="grow">
                        <Machine machine={props.subject.mech} />
                    </section>
                    <section>
                        <h3>{compilation()?.source.file}: {compilation()?.source.line}</h3>
                        <CodeBlock lang="python">{compilation()?.source.block}</CodeBlock>
                    </section>
                    <section>
                        <CodeBlock lang="rel">
                            {compilation()?.emitted}
                        </CodeBlock>
                    </section>
                    <section>
                        <h3>IR</h3>
                        <CodeBlock>
                            {props.subject.task}
                        </CodeBlock>
                    </section>
                    {props.children}
                </scroll-inner>
            </scroll-container>
        </span-viewer>
    )
}


export interface RuleViewerProps {
    subject: Span.Rule;
}
export function RuleViewer(props: RuleViewerProps) {
    return (
        <BlockViewer subject={props.subject}>
        </BlockViewer>
    )
}

export interface QueryViewerProps {
    subject: Span.Query;
}
export function QueryViewer(props: QueryViewerProps) {
    const results = () => props.subject.events.find(Message.is_time)?.results
    return (
        <BlockViewer subject={props.subject}>
            <Show when={results()}>
                <section>
                    <h3>Results ({results()?.values.length} / {results()?.count})</h3>
                    <table>
                        <thead>
                            <tr>
                                <For each={Object.keys(results()?.values[0] ?? {})}>
                                    {(key) => <td>{key}</td>}
                                </For>
                            </tr>
                        </thead>
                        <tbody>
                            <For each={results()?.values}>
                                {(row) => (
                                    <tr>
                                        <For each={Object.entries(row)}>
                                            {([key, value]) => <td>{value}</td>}
                                        </For>
                                    </tr>
                                )}
                            </For>
                        </tbody>
                    </table>
                </section>
            </Show>
        </BlockViewer>
    )
}

export interface PlaceholderViewerProps {
    subject: Placeholder;
}
export function PlaceholderViewer(props: PlaceholderViewerProps) {
    return (
        <span-viewer class="placeholder">
            <scroll-container>
                <scroll-inner>
                    Waiting for block {props.subject.selection_path.slice(1)}
                </scroll-inner>
            </scroll-container>
        </span-viewer>
    );
}


export interface UnknownViewerProps {
    subject: Span;
}
export function UnknownViewer(props: UnknownViewerProps) {
    return (
        <span-viewer>
            <scroll-container>
                <scroll-inner>
                    <CodeBlock lang="json">
                        {JSON.stringify(props.subject, null, 4)}
                    </CodeBlock>
                </scroll-inner>
            </scroll-container>
        </span-viewer>
    )
}



const viewers = {
    "rule": RuleViewer,
    "query": QueryViewer,
    "placeholder": PlaceholderViewer
};

export interface EventViewerProps {
    subject: Subject;
}
export function EventViewer(props: EventViewerProps) {
    const component = () =>
        viewers[props.subject.span_type as keyof typeof viewers]
        ?? viewers[props.subject.event as keyof typeof viewers]
        ?? UnknownViewer;
    return (
        <Dynamic component={component()} subject={props.subject as any} />
    )
}
