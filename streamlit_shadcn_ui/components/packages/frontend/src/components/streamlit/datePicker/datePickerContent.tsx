import { Button } from "@/components/ui/button";
import { Calendar } from "@/components/ui/calendar";
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover";
import { useBodyStyle } from "@/hooks/useBodyStyle";
import { format, parse } from "date-fns";
import { forwardRef, useEffect, useState, useCallback, useMemo, useRef, useLayoutEffect } from "react";
import { Streamlit } from "streamlit-component-lib";

// Improved hook for measuring height with debouncing
function useMeasureHeight(selector: string, forwardedRef: React.ForwardedRef<HTMLElement>, padding = 10) {
    // Track if we've already measured to avoid double measurements
    const hasMeasuredRef = useRef(false);
    const timeoutRef = useRef<number | null>(null);

    const measureAndSetHeight = useCallback(() => {
        // Clear any pending measurement
        if (timeoutRef.current) {
            clearTimeout(timeoutRef.current);
        }

        // Debounce measurements to prevent multiple rapid calls
        timeoutRef.current = window.setTimeout(() => {
            // Try all possible ways to get the height
            const forwardedRefHeight = forwardedRef &&
                typeof forwardedRef !== "function" &&
                forwardedRef.current?.offsetHeight;

            const domElement = document.querySelector(selector);
            const domElementHeight = (domElement as HTMLElement)?.offsetHeight;

            // Use either ref.current or directly query for the element
            const currentHeight = forwardedRefHeight || domElementHeight || 300;

            // Set frame height only if it's different from before
            Streamlit.setFrameHeight(currentHeight + padding);

            // Mark as measured
            hasMeasuredRef.current = true;
            timeoutRef.current = null;
        }, 50); // 50ms debounce
    }, [forwardedRef, selector, padding]);

    // Cleanup timeout on unmount
    useEffect(() => {
        return () => {
            if (timeoutRef.current) {
                clearTimeout(timeoutRef.current);
            }
        };
    }, []);

    return { measureAndSetHeight, hasMeasured: hasMeasuredRef };
}

type DateRange = {
    from: Date;
    to?: Date;
};

const formatDate = (date: Date | DateRange | string | string[]): string | [string, string] => {
    const formatSingleDate = (date: Date) => {
        return format(date, "yyyy-MM-dd");
    }
    if (date instanceof Date) {
        return formatSingleDate(date);
    } else if (typeof date === "string") {
        const d = parse(date, 'yyyy-MM-dd', new Date());
        return formatSingleDate(d);
    } else if (Array.isArray(date)) {
        return [formatDate(date[0]), formatDate(date[1])] as [string, string];
    } else {
        return [formatDate(date.from), formatDate(date.to)] as [string, string];
    }
}

type StDatePickerContentProps =
    | {
        value?: string;
        mode: "single";
        open?: boolean;
    }
    | {
        value?: [string, string];
        mode: "range";
        open?: boolean;
    };

const initDateValue = (props: StDatePickerContentProps): Date | DateRange => {
    const { value, mode } = props;
    if (mode === "single") {
        return value ? parse(value, 'yyyy-MM-dd', new Date()) : new Date();
    } else {
        if (!value) {
            return {
                from: new Date(),
            };
        }
        return {
            from: parse(value[0], 'yyyy-MM-dd', new Date()),
            to: parse(value[1], 'yyyy-MM-dd', new Date()),
        };
    }
}

export const StDatePickerContent = forwardRef<
    HTMLDivElement,
    StDatePickerContentProps
>((props, ref) => {
    const { value, mode, open = true } = props;

    // Create a unique instance ID to track this component
    const instanceId = useRef(`dp-${Math.random().toString(36).substring(2, 9)}`);

    // Use memoized initial date value to prevent unnecessary recalculations
    const initialDate = useMemo(() => initDateValue(props), []);
    const [date, setDate] = useState<Date | DateRange>(initialDate);

    // Use internal state to ensure UI updates immediately
    const [isOpen, setIsOpen] = useState(open);

    // Create a local ref that we control completely
    const localRef = useRef<HTMLDivElement | null>(null);

    // Store component mount status
    const isMounted = useRef(false);

    // Use ref for stable callback references
    const propsRef = useRef(props);
    propsRef.current = props;

    // Track if we've already sent a value to Streamlit to prevent duplicates
    const hasReportedRef = useRef(false);

    // Sync internal open state with prop - but only once on mount
    useEffect(() => {
        if (!isMounted.current) {
            setIsOpen(open);
            isMounted.current = true;
        }
    }, [open]);

    // Use the custom hook for measuring height
    const { measureAndSetHeight, hasMeasured } = useMeasureHeight('.date-picker-content', ref);

    // Only update date when value or mode changes
    useEffect(() => {
        if (isMounted.current) {
            setDate(initDateValue({
                value,
                mode,
            } as StDatePickerContentProps));
        }
    }, [value, mode]);

    useBodyStyle("body, document { background-color: transparent !important; }");

    // Memoize action handler to prevent recreating on each render
    const handleAction = useCallback((confirm: boolean) => {
        // Prevent duplicate reports
        if (hasReportedRef.current) return;

        // Mark as reported
        hasReportedRef.current = true;

        // Close the popover immediately in UI
        setIsOpen(false);

        // Get current values from ref to ensure latest props
        const currentProps = propsRef.current;

        // Log what we're sending (for debugging)
        console.log(`[DatePicker ${instanceId.current}] Sending value:`,
            confirm ? formatDate(date) : (currentProps.value || null));

        // Send the update to Streamlit
        Streamlit.setComponentValue({
            value: confirm ? formatDate(date) : (currentProps.value || null),
            open: false,
            instance_id: instanceId.current,
        });
    }, [date]);

    // Handle cleanup on unmount
    useEffect(() => {
        return () => {
            // If component unmounts without reporting, send the cancel action
            if (!hasReportedRef.current) {
                console.log(`[DatePicker ${instanceId.current}] Cleanup - sending cancel`);
                Streamlit.setComponentValue({
                    value: propsRef.current.value || null,
                    open: false,
                    instance_id: instanceId.current,
                });
            }
        };
    }, []);

    // Combine external ref with our local ref
    const combineRefs = useCallback((node: HTMLDivElement | null) => {
        // Update our local ref
        localRef.current = node;

        // Forward to external ref
        if (typeof ref === 'function') {
            ref(node);
        } else if (ref) {
            ref.current = node;
        }

        // Only measure height if we haven't already or if the node changed
        if (node && (!hasMeasured.current || node !== localRef.current)) {
            measureAndSetHeight();
        }
    }, [ref, measureAndSetHeight]);

    // If not open according to internal state, render nothing
    if (!isOpen) {
        return null;
    }

    return (
        <Popover open={isOpen} onOpenChange={(open) => {
            // This will handle external (escape key) closing
            if (!open && !hasReportedRef.current) {
                handleAction(false);
            }
        }}>
            <PopoverTrigger className="hidden" />
            <PopoverContent
                className="date-picker-content w-auto p-0"
                ref={combineRefs}
            >
                {mode === 'single' && (
                    <Calendar
                        mode="single"
                        selected={date as Date}
                        onSelect={(newDate) => {
                            if (newDate) {
                                setDate(newDate as Date);
                                measureAndSetHeight();
                            }
                        }}
                        initialFocus
                    />
                )}

                {mode === 'range' && (
                    <Calendar
                        mode="range"
                        selected={date as DateRange}
                        onSelect={(newDate) => {
                            if (newDate) {
                                setDate(newDate as DateRange);
                                measureAndSetHeight();
                            }
                        }}
                        initialFocus
                    />
                )}

                <div className="mb-4 mx-4 flex gap-2">
                    <Button onClick={() => handleAction(true)}>
                        Pick
                    </Button>
                    <Button variant="secondary" onClick={() => handleAction(false)}>
                        Cancel
                    </Button>
                </div>
            </PopoverContent>
        </Popover>
    );
});