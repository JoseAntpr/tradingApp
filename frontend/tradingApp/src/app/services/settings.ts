import { InjectionToken, ValueProvider } from '@angular/core';
import { environment } from '../../environments/environment'

export const BackendUri: InjectionToken<string> = new InjectionToken<string>('BackendUri');



export const BackendUriProvider: ValueProvider = {
    provide: BackendUri,
    useValue: environment.urlBackend
}