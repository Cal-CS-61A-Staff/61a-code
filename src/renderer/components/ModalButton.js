import React from "react";

export default function ModalButton({ children, buttonText, onClick }) {
    return (
        <div className="modalCol">
            {children
            && (
                <p>
                    {children}
                </p>
            )
            }
            <button
                className="fileDownloadBtn"
                type="button"
                onClick={onClick}
            >
                {buttonText}
            </button>
        </div>
    );
}
