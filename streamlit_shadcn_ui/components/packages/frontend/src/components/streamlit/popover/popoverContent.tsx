import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover"

import { forwardRef, useEffect, useRef, useState } from "react";
import { Streamlit } from "streamlit-component-lib";
import { useBodyStyle } from "@/hooks/useBodyStyle";

interface StPopoverContentProps {
    content: string;
}
export const StPopoverContent = forwardRef<HTMLDivElement, StPopoverContentProps>((props, forwardedRef) => {
    const { content } = props;

    // Create a local ref as fallback
    const localRef = useRef<HTMLDivElement>(null);
    // Keep track of whether the content is mounted
    const [isMounted, setIsMounted] = useState(false);

    // Force a reflow after component mounts to ensure height calculation works
    useEffect(() => {
        // Set a small timeout to ensure the component is fully rendered
        const timer = setTimeout(() => {
            setIsMounted(true);
        }, 50);

        return () => clearTimeout(timer);
    }, []);

    // Effect to set the frame height whenever the content is mounted
    useEffect(() => {
        if (!isMounted) return;

        console.log("PopoverContent refs", { forwardedRef, localRef });

        // Try to get the content element directly if refs don't work
        const popoverContent = document.querySelector('.popover-content');

        // Use either ref.current or directly query for the element
        const currentHeight =
            (forwardedRef && typeof forwardedRef !== "function" && forwardedRef.current?.offsetHeight) ||
            localRef.current?.offsetHeight ||
            (popoverContent as HTMLElement)?.offsetHeight ||
            50; // Fallback minimum height

        console.log("Setting height to", currentHeight + 5);
        Streamlit.setFrameHeight(currentHeight + 5);
    }, [forwardedRef, isMounted]);

    useBodyStyle("body { background-color: transparent !important; }");

    return (
        <Popover open={true}>
            <PopoverTrigger className="hidden" />
            <PopoverContent
                ref={(node) => {
                    // Update both refs
                    if (typeof forwardedRef === 'function') {
                        forwardedRef(node);
                    } else if (forwardedRef) {
                        forwardedRef.current = node;
                    }
                    localRef.current = node;
                }}
                className="popover-content"
            >
                {content}
            </PopoverContent>
        </Popover>
    )
});
