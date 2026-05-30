describe('PokeAPI', () => {

  it('Caso 1: Validación de berry 1', () => {
      // 1. Hacemos el GET a la PokeAPI
    cy.request('GET', 'https://pokeapi.co/api/v2/berry/1')
    .then((response) => {
      
      // 2. Verificación que el size sea 20
      expect(response.body.size).to.eq(20)

      // 3. Verificación que el soil_dryness sea 15
      expect(response.body.soil_dryness).to.eq(15)

      // 4. Verificación que en firmness, el name sea soft
      expect(response.body.firmness.name).to.eq('soft')

    })
  })

  it('Caso 2: Valadicación de berry 2', () =>{
      // 1. Hacemos el GET a la PokeAPI
    cy.request('GET', 'https://pokeapi.co/api/v2/berry/2')
    .then((response) => {

      // 2. Verificación que en firmeness, el name sea super-hard
      expect(response.body.firmness.name).to.eq('super-hard')

      // 3. Verificación el size sea mayor al anterior
      expect(response.body.size).to.be.greaterThan(20)

      // 4. Verificación que el soil_dryness sea igual que el anterior
      expect(response.body.soil_dryness).to.eq(15)

    })
  })

  it('Caso 3: Valadicación pikachu', () =>{
      // 1. Hacemos el GET a la PokeAPI
    cy.request('GET', 'https://pokeapi.co/api/v2/pokemon/pikachu/')
    .then((response) => {

      // 2. Verificación de su experiencia
      expect(response.body.base_experience).to.be.greaterThan(10).and.to.be.lessThan(1000)

      // 3. Verificación que su tipo es electric
      expect(response.body.types[0].type.name).to.eq('electric')

    })
  })
})