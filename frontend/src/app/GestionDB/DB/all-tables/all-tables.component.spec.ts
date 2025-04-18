import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllTablesComponent } from './all-tables.component';

describe('AllTablesComponent', () => {
  let component: AllTablesComponent;
  let fixture: ComponentFixture<AllTablesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AllTablesComponent]
    });
    fixture = TestBed.createComponent(AllTablesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
