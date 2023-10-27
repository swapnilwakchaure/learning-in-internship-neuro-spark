// post the address into saved_address database
savedAddressRoute.post("/", async (req, res) => {

    let { shipping_country, shipping_state, shipping_city, country, state, city, ...payload } = req.body;
  
    payload.shipping_country_id = shipping_country;
    payload.shipping_state_id = shipping_state;
    payload.shipping_city_id = shipping_city;
    payload.country_id = country;
    payload.state_id = state;
    payload.city_id = city;
  
    payload.country_name = await getCountryById(country);
    payload.state_name = await getStateById(country, state);
    payload.city_name = await getCityById(state, city);
    payload.shipping_country_name = await getCountryById(shipping_country);
    payload.shipping_state_name = await getStateById(shipping_country, shipping_state);
    payload.shipping_city_name = await getCityById(shipping_state, shipping_city);
  
    try {
    const old_saved_address = await Saved_Address.findAll({
      where: {
        id: req.body.id
      }
    });
    if (old_saved_address.length === 0) {
      let new_user_address = new Saved_Address(payload);
      await new_user_address.save();
      res
        .status(200)
        .send(
          `address saved successfully`
        );
    } else {
      const { first_name, middle_name, last_name, company, address_line_1, address_line_2, landmark, city_id, state_id, country_id, pincode, phone, email, shipping_first_name, shipping_middle_name, shipping_last_name, shipping_company, shipping_address_line_1, shipping_address_line_2, shipping_landmark, shipping_city_id, shipping_state_id, shipping_country_id, shipping_pincode, shipping_phone, shipping_email } = payload;
  
      const same_address = await Saved_Address.findOne({
        where: {
          first_name,
          middle_name,
          last_name,
          company,
          address_line_1,
          address_line_2,
          landmark,
          city_id,
          state_id,
          country_id,
          pincode,
          phone,
          email,
          shipping_first_name,
          shipping_middle_name,
          shipping_last_name,
          shipping_company,
          shipping_address_line_1,
          shipping_address_line_2,
          shipping_landmark,
          shipping_city_id,
          shipping_state_id,
          shipping_country_id,
          shipping_pincode,
          shipping_phone,
          shipping_email
        }
      })
  
      if (same_address) {
        console.log('data is available in the database');
        return res.status(200).send('data is available in the database');
      } else {
        const new_address = new Saved_Address(payload);
        await new_address.save();
        res.status(201).send(`${first_name} ${last_name}, you're address successfully saved`);
      }
    }
  } catch (error) {
    // console.log("error: ", error);
    res.status(404).send(`error: ${error}`);
  }
  });