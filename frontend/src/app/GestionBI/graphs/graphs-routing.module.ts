// graphs-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DataAnalysisComponent } from './data-analysis/data-analysis.component';

const routes: Routes = [
  { path: '', component: DataAnalysisComponent },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class GraphsRoutingModule { }
