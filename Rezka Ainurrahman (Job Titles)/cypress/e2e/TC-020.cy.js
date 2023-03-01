import { faker } from '@faker-js/faker';

//Add job title with numbers in all field
describe('failed_addjobtitle', () => {
    it('failed_addjobtitle', () => {
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
      cy.get(':nth-child(2) > .oxd-input').type('1234567890')//input job title
      cy.get(':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-textarea').type(`1234567890`)//input job deskripsi
      cy.get('.oxd-file-div').attachFile(file)//input job specification
      cy.get(':nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-textarea').type(`1234567890`)//input note
      cy.get('.oxd-button--secondary').click()//save

      cy.wait(2000)
      cy.get('.orangehrm-container').contains('1234567890').should('exist')
    })
  })