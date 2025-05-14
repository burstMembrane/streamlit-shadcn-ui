import {
    AlertDialog,
    AlertDialogAction,
    AlertDialogCancel,
    AlertDialogContent,
    AlertDialogDescription,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogTitle,
    AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { Button } from "@/components/ui/button";
import { useBodyStyle } from "@/hooks/useBodyStyle";
import { forwardRef, useEffect, useRef, useCallback } from "react";
import { Streamlit } from "streamlit-component-lib";

// Custom hook for measuring and setting component height
function useMeasureHeight(selector: string, forwardedRef: React.ForwardedRef<HTMLElement>, padding = 10) {
    const measureAndSetHeight = useCallback(() => {
        // Try all possible ways to get the height
        const forwardedRefHeight = forwardedRef &&
            typeof forwardedRef !== "function" &&
            forwardedRef.current?.offsetHeight;

        const domElement = document.querySelector(selector);
        const domElementHeight = (domElement as HTMLElement)?.offsetHeight;

        // Use either ref.current or directly query for the element
        const currentHeight = forwardedRefHeight || domElementHeight || 300;

        Streamlit.setFrameHeight(currentHeight + padding);
    }, [forwardedRef, selector, padding]);

    // Effect to run the measurement
    useEffect(() => {
        if (!forwardedRef) {
            return;
        }

        // Initial measurement
        measureAndSetHeight();

        // Optionally add a delayed measurement if needed
        // const timer = setTimeout(measureAndSetHeight, 50);
        // return () => clearTimeout(timer);
    }, [forwardedRef, measureAndSetHeight]);

    return measureAndSetHeight;
}

interface StAlertDialogProps {
    title?: string;
    description?: string;
    confirmLabel?: string;
    cancelLabel?: string;
}
export const StAlertDialog = forwardRef<HTMLDivElement, StAlertDialogProps>(
    (props, forwardedRef) => {
        const {
            title,
            description,
            confirmLabel = "Confirm",
            cancelLabel = "Cancel",
        } = props;

        // Use the custom hook
        const measureAndSetHeight = useMeasureHeight('.alert-dialog-content', forwardedRef);

        useBodyStyle(
            "body { background-color: transparent !important; padding-right: 0.5em !important; }"
        );

        const handleAction = (confirm: boolean) => {
            Streamlit.setComponentValue({
                confirm,
                open: false,
            });
        };

        return (
            <AlertDialog open={true}>
                <AlertDialogTrigger asChild>
                    <Button variant="outline">Show Dialog</Button>
                </AlertDialogTrigger>
                <AlertDialogContent
                    ref={(node) => {
                        if (typeof forwardedRef === 'function') {
                            forwardedRef(node);
                        } else if (forwardedRef) {
                            forwardedRef.current = node;
                        }
                        // Call measureAndSetHeight when the ref is set
                        if (node) {
                            setTimeout(measureAndSetHeight, 0);
                        }
                    }}
                    className="alert-dialog-content m-1"
                >
                    <AlertDialogHeader>
                        <AlertDialogTitle>{title}</AlertDialogTitle>
                        <AlertDialogDescription>
                            {description}
                        </AlertDialogDescription>
                    </AlertDialogHeader>
                    <AlertDialogFooter>
                        <AlertDialogCancel
                            onClick={() => {
                                handleAction(false);
                            }}
                        >
                            {cancelLabel}
                        </AlertDialogCancel>
                        <AlertDialogAction
                            onClick={() => {
                                handleAction(true);
                            }}
                        >
                            {confirmLabel}
                        </AlertDialogAction>
                    </AlertDialogFooter>
                </AlertDialogContent>
            </AlertDialog>
        );
    }
);
