import * as React from "react";

export default function PositionSlider(props) {
    return (
        <div className="pyPosSlider">
            <input
                type="range"
                min={0}
                max={props.num}
                value={props.value}
                step={1}
                className="pyPosSliderElem"
                onChange={props.onChange}
            />
        </div>
    );
}

// PositionSlider.propTypes = {
//     onChange: PropTypes.func,
//     value: PropTypes.number,
//     num: PropTypes.number,
// };
