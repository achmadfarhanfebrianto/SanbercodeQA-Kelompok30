import { faker } from '@faker-js/faker';

//Add job title without fill Job Specificatio field
describe('successfull_deletejobtitle', () => {
    it('successfull_deletejobtitle', () => {
      var username=':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input'
      var password=':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input'
      let jobTitle = faker.name.jobTitle();
      var file = 'pdf-file.pdf'

      cy.visit('/')
      cy.get(username).type("Admin")
      cy.get(password).type("admin123")
      cy.get('.oxd-button').click()
      cy.wait(2000) 
      cy.get('.oxd-topbar-header-title').should('exist')//validasi login
  
      cy.get(':nth-child(1) > .oxd-main-menu-item > .oxd-text').click()//klik admin
      cy.wait(1000) 
      cy.get(':nth-child(2) > .oxd-topbar-body-nav-tab-item').click()//klik job
      cy.wait(1000) 
      cy.get('.oxd-dropdown-menu > :nth-child(1)').click()//klik job title
      cy.scrollTo(0, 0)
           
      cy.get(':nth-child(2) > .oxd-table-row > [style="flex: 2 1 0%;"] > div').then(($btn) => {
        const jobName = $btn.text()
        cy.get(':nth-child(2) > .oxd-table-row > [style="flex: 1 1 0%;"] > .oxd-table-cell-actions > :nth-child(1)').click()
        cy.get('.oxd-button--label-danger > .oxd-icon').click()

        cy.get(jobName).should('not.exist');//validasi sukses hapus job title
      })
    })
  })