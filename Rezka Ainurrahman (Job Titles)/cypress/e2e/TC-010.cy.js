import { faker } from '@faker-js/faker';

//Add job title only with fill Job Description field
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
      cy.get(':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-textarea').type(`This is new ${jobTitle}`)//input job deskripsi
      cy.get('.oxd-button--secondary').click()//save
      cy.wait(1000)

      cy.get('.oxd-input-group > .oxd-text').should('exist')//validasi tidak bisa add job title
    })
  })