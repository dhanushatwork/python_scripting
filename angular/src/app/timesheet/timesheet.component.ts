import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-timesheet',
  templateUrl: './timesheet.component.html',
  styleUrls: ['./timesheet.component.css']
})
export class TimesheetComponent {
  timesheet = {
    username: '',
    date: '',
    hoursLogged: 0,
    taskDetail: ''
  };

  constructor(private http: HttpClient) {}

  
  submitTimesheet() {
    this.http.post('http://localhost:8080/api/timesheets/add', this.timesheet)
      .subscribe(response => {
        console.log('Timesheet submitted:', response);
      }, error => {
        console.error('Error submitting timesheet:', error);
      });
  }
}
