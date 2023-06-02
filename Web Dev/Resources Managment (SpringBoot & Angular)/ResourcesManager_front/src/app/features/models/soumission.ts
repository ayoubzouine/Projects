import { Offre } from "./offre";

export interface Soumission {
    id?:number; 
    marqueOrdinateur?:string; 
    marqueImprimante?:string ; 
    prix:number;
    etat?:number;   
    offreDto:Offre; 
}
