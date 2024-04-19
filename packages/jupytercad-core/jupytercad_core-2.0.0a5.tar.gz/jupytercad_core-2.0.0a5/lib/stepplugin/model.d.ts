import { IJCadObject, IJcadObjectDocChange, IJupyterCadDoc, JupyterCadDoc } from '@jupytercad/schema';
import { ISignal } from '@lumino/signaling';
export declare class JupyterCadStepDoc extends JupyterCadDoc {
    constructor();
    get version(): string;
    get objectsChanged(): ISignal<IJupyterCadDoc, IJcadObjectDocChange>;
    get objects(): Array<IJCadObject>;
    static create(): JupyterCadStepDoc;
    editable: boolean;
    exportable: boolean;
    private _sourceObserver;
    private _source;
    private _objectChanged;
}
