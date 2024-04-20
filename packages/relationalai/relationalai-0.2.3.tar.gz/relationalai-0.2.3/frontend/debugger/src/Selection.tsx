import { createContext, createSignal, type Accessor, type Setter } from "solid-js";
import type { Span, Subject } from "./debugger_client";

//------------------------------------------------------------------------------
// Selection
//------------------------------------------------------------------------------

export class Selection<T> {
    selected: Accessor<T[]>;
    protected set_selected: Setter<T[]>;

    constructor(public name: string) {
        [this.selected, this.set_selected] = createSignal<T[]>([]);
    }

    primary(): T|undefined {
        return this.selected()[0];
    }

    last(): T|undefined {
        const cur = this.selected();
        return cur[cur.length - 1];
    }

    is_selected(v: any): boolean {
        return this.selected().includes(v);
    }

    clear = () => this.set_selected([]);

    select = (v: T) => this.set_selected([v]);

    add = (v: T) => {
        const cur = this.selected();
        if (cur.includes(v)) return;
        this.set_selected([...cur, v]);
        return this;
    }

    remove = (v: T) => {
        const cur = this.selected();
        let ix = cur.indexOf(v);
        if (ix === -1) return;
        this.set_selected(cur.toSpliced(ix, 1));
    }
}

export function createSelectionContext<T>(name: string) {
    return createContext(new Selection<T>(name));
}

//------------------------------------------------------------------------------
// Global selection pools
//------------------------------------------------------------------------------

export const EventListSelection = createSelectionContext<Subject>("EventList");
export const EventDetailSelection = createSelectionContext<Subject>("EventDetail");
