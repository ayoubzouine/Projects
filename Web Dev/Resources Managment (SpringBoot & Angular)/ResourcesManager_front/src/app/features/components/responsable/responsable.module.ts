import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListeRessourcesComponent } from './liste-ressources/liste-ressources.component';
import { ResponsableRoutingModule } from './responsable-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ResourceDetailComponent } from './resource-detail/resource-detail.component';
import { OffreComponent } from './offre/offre.component';
import { ConsulterFournisseurComponent } from './consulter-fournisseur/consulter-fournisseur.component';
import { ConsulterPannesComponent } from './consulter-pannes/consulter-pannes.component';
import { ListDemandsComponent } from '../director/list-demands/list-demands.component';
import { NewDemandComponent } from '../director/new-demand/new-demand.component';
import { UpdateDemandComponent } from '../director/update-demand/update-demand.component';



@NgModule({
  declarations: [
    ListeRessourcesComponent,
    ResourceDetailComponent,
    OffreComponent,
    ConsulterFournisseurComponent,
    ConsulterPannesComponent,
  ],
  imports: [
    CommonModule,
    ResponsableRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ]
})
export class ResponsableModule { }
