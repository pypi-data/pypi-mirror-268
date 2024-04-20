import {Button as KButton} from "@kobalte/core";
import { JSXElement, Match, Switch, splitProps } from "solid-js";
import {Tooltip} from "./Tooltip";
import "./Button.styl";

export interface ButtonProps extends KButton.ButtonRootProps {
    tooltip?: JSXElement
}
export function Button(props: ButtonProps) {
    const [local, remote] = splitProps(props, ["class", "tooltip"]);
    return (
        <Switch>
            <Match when={local.tooltip}>
                <Tooltip content={local.tooltip}>
                    <Tooltip.Trigger as={KButton.Root} class={`ui-button ${local.class || ""}`} {...remote} />
                </Tooltip>
            </Match>
            <Match when={true}>
                <KButton.Root class={`ui-button ${local.class || ""}`} {...remote} />
            </Match>
        </Switch>
    )
}
