import React, { useState } from "react";
import { dialogWrap } from "../utils/dialogWrap.js";
import CardList from "./CardList.js";
import { getBackups } from "../../web/filesystem.js";
import { useAsync } from "../utils/hooks.js";

function OKBackupsDialog({ assignments, onFileSelect }) {
    const [selectedIndex, setSelectedIndex] = useState(null);
    const selected = selectedIndex === null ? null : assignments[selectedIndex];

    const backups = useAsync(
        () => (selected ? getBackups(selected.name) : null),
        null, [selected],
    );

    let header;
    if (selected == null) {
        header = "Backups";
    } else if (backups === null) {
        header = "Loading...";
    } else if (backups.length === 0) {
        header = "No backups found for assignment.";
    } else {
        header = "Backups";
    }

    return (
        <>
            <CardList
                header="Assignments"
                items={assignments.map(({ display_name: displayName }) => displayName)}
                onClick={i => setSelectedIndex(i)}
                selectedIndex={selectedIndex}
            />
            <CardList
                header={header}
                items={backups ? backups.map(x => x.name) : []}
                onClick={i => onFileSelect(backups[i])}
            />
        </>
    );
}

export default dialogWrap("OKPy Backups", OKBackupsDialog, "row");
