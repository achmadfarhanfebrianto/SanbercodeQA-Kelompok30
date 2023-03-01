import { faker } from '@faker-js/faker';

//Add job title with add exceed 100 characters Job Title field
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
      cy.get(':nth-child(2) > .oxd-input').type("Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry's standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book It has survived not only five centuries but also the leap into electronic typesetting remaining essentially unchanged It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")//input job title
      cy.get(':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-textarea').type(`This is new ${jobTitle}`)//input job deskripsi
      cy.get('.oxd-file-div').attachFile(file)//input job specification
      cy.get(':nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-textarea').type(`New Position`)//input note
      cy.get('.oxd-button--secondary').click()//save
      cy.wait(1000)
      
      cy.get('.oxd-input-group > .oxd-text').should('exist')//validasi tidak bisa add job title
    })
  })