import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router'; // Add this import

import { AppComponent } from './app.component';
import { TimesheetComponent } from './timesheet/timesheet.component';

// Define your routes
const routes: Routes = [
  { path: 'timesheet', component: TimesheetComponent },
  { path: '', redirectTo: '/timesheet', pathMatch: 'full' } // Default route
];

@NgModule({
  declarations: [
    AppComponent,
    TimesheetComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes) // Register RouterModule with routes
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
