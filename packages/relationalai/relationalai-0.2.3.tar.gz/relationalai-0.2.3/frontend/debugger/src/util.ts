export function ends_in<T>(list: T[], one_of: T[]) {
    if(list.length === 0) return false;

    let last = list[list.length - 1];
    for(let v of one_of) {
        if(v === last) return true;
    }
    return false;
}

export function prefix_of<T>(list: T[], prefix: T[]) {
    if(list.length < prefix.length) return false;
    for(let ix = 0; ix < prefix.length; ix += 1) {
        if(list[ix] !== prefix[ix]) return false;
    }
    return true;
}

function fallback_copy_text_to_clipboard(text: string): Promise<void> {
    var textArea = document.createElement('textarea');
    textArea.value = text;

    // Avoid scrolling to bottom
    textArea.style.top = '0';
    textArea.style.left = '0';
    textArea.style.position = 'fixed';

    return new Promise<void>((resolve, reject) => {
        try {
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();

            var successful = document.execCommand('copy');
            setTimeout(() => successful ? resolve() : reject(), 1);
        } catch (err) {
            setTimeout(() => reject(err), 1);
        }
        document.body.removeChild(textArea);
    });
}

export async function copy_text_to_clipboard(text: string): Promise<void> {
    try {
        await navigator.clipboard.writeText(text);
        return;
    } catch {
        await fallback_copy_text_to_clipboard(text);
    }
}


const time_formatter_ms = new Intl.NumberFormat("en", {style: "unit", unit: "millisecond", unitDisplay: "short", maximumFractionDigits: 1});
const time_formatter_s = new Intl.NumberFormat("en", {style: "unit", unit: "second", unitDisplay: "short", maximumFractionDigits: 2});

export const fmt = {
    time: {
        ms(v: number) {
            return time_formatter_ms.format(v);
        },
        s(v: number) {
            return time_formatter_s.format(v);
        }
    }
}
