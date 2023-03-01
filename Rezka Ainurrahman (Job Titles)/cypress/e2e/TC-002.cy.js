import { faker } from '@faker-js/faker';

//Add job title without fill Job Description field
describe('successfull_addjobtitle', () => {
    it('successfull_addjobtitle', () => {
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
      cy.scrollTo('top')
      cy.get('.orangehrm-header-container > .oxd-text').should('exist')//validasi job title

      cy.get('.oxd-button > .oxd-icon').click() //klik +add
      cy.get(':nth-child(2) > .oxd-input').type(jobTitle)//input job title
      cy.get('.oxd-file-div').attachFile(file)//input job specification
      cy.get(':nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-textarea').type(`New Position`)//input note
      cy.get('.oxd-button--secondary').click()//save

      cy.wait(2000)
      cy.get('.orangehrm-container').contains(jobTitle).should('exist')//validasi sukses add job title
    })
  })