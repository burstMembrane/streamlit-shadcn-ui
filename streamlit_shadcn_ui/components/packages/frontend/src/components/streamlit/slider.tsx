import { forwardRef, useState } from "react";
import { Streamlit } from "streamlit-component-lib";
import { Slider } from "@/components/ui/slider";
import { cn } from "@/lib/utils";

interface StSliderProps {
    defaultValue?: number[];
    max?: number;
    min?: number;
    step?: number;
    label?: string;
    className?: string;
}

export const StSlider = forwardRef<HTMLDivElement, StSliderProps>(
    (props: StSliderProps, ref) => {
        const { defaultValue, max, min, step, label, className } = props;
        const [sliderValue, setSliderValue] = useState<number[]>(defaultValue || [0]);

        // Handle slider value change
        const handleSliderChange = (value: number[]) => {
            setSliderValue(value);
            Streamlit.setComponentValue(value);
        };

        return (
            <div ref={ref} className={cn("flex flex-col space-y-2 m-1", className)}>
                {label && <label>{label}</label>}
                <Slider
                    defaultValue={defaultValue}
                    value={sliderValue}
                    max={max || 100}
                    min={min || 0}
                    step={step || 1}
                    onValueChange={handleSliderChange}
                    className="w-full"
                />
            </div>
        );
    }
);
