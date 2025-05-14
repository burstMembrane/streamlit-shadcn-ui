import { forwardRef, useEffect } from "react";
import { Popover, PopoverContent, PopoverTrigger } from "../ui/popover";
import { Streamlit } from "streamlit-component-lib";

interface StPopoverProps {
    text?: string;
    disabled?: boolean;
    onClick?: () => void;
}
export const StPopover = forwardRef<HTMLDivElement>(
    (props: StPopoverProps, ref) => {
        const { text, disabled, onClick } = props;
        useEffect(() => {
            console.log("Popover ref", ref);
            if (ref && typeof ref !== "function" && ref.current?.offsetHeight) {
                Streamlit.setFrameHeight(ref.current.offsetHeight + 10);
            }
        }, [ref])
        return (
            <Popover>
                <PopoverTrigger>Open</PopoverTrigger>
                <div ref={ref}>TTT</div>
                <PopoverContent>
                    Place content for the popover here.
                </PopoverContent>
            </Popover>
        );
    }
);
