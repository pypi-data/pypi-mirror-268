import { Collapsible as KCollapsible } from "@kobalte/core";
import { JSXElement, splitProps } from "solid-js";
import { Icon } from "./Icon";
import "./Collapsible.styl";
import { Button } from "./Button";

export function CollapsibleTrigger(props: KCollapsible.CollapsibleTriggerProps) {
    let [local, remote] = splitProps(props, ["class", "children"]);
    return (
        <KCollapsible.Trigger as={Button} class={`ui-collapsible-trigger ${local.class ?? ""}`} {...remote}>
            {local.children}
        </KCollapsible.Trigger>
    )
}

export function CollapsibleTriggerIcon() {
    return (
        <Icon name="chevron-down" class="ui-collapsible-trigger-icon" />
    )
}

export function CollapsibleContent(props: KCollapsible.CollapsibleContentProps) {
    let [local, remote] = splitProps(props, ["class", "children"]);
    return (
        <KCollapsible.Content class={`ui-collapsible-content ${local.class ?? ""}`} {...remote}>
            <div class="ui-collapsible-inner">
                {local.children}
            </div>
        </KCollapsible.Content>
    )
}

export interface CollapsibleProps extends KCollapsible.CollapsibleRootProps {
    class?: string,
    side: "right" | "left" | "bottom" | "top"
    children: JSXElement
}
export function Collapsible(props: CollapsibleProps) {
    let [local, remote] = splitProps(props, ["class", "side", "children"]);
    return (
        <KCollapsible.Root {...remote} class={`ui-collapsible ${local.side} ${local.class ?? ""}`}>
            {local.children}
        </KCollapsible.Root>
    )
}
Collapsible.Trigger = CollapsibleTrigger;
Collapsible.TriggerIcon = CollapsibleTriggerIcon;
Collapsible.Content = CollapsibleContent;
