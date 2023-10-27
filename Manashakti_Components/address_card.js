import React from "react";
import "./AddressCard.css";
import { RiDeleteBin6Fill } from "react-icons/ri";

export default function AddressCard({
  data,
  selectAddressId,
  handleSetFormFields,
  handleDeleteAddress,
}) {
  const {
    id,
    address_line_1,
    address_line_2,
    city_id,
    city_name,
    company,
    country_id,
    country_name,
    email,
    first_name,
    landmark,
    last_name,
    middle_name,
    phone,
    pincode,
    shipping_address_line_1,
    shipping_address_line_2,
    shipping_city_id,
    shipping_city_name,
    shipping_company,
    shipping_country_id,
    shipping_country_name,
    shipping_email,
    shipping_first_name,
    shipping_landmark,
    shipping_last_name,
    shipping_middle_name,
    shipping_phone,
    shipping_pincode,
    shipping_state_id,
    shipping_state_name,
    state_id,
    state_name,
  } = data;

  return (
    <>
      <div
        className="address_card_container"
        style={{
          display:
            selectAddressId === null || id === selectAddressId
              ? "block"
              : "none",
        }}
      >
        <div
          className="saved_address_card_page"
          onClick={() => handleSetFormFields(data)}
        >
          {/* shipping address */}
          <div>
            <h4>Shipping Address</h4>
            <p className="address_user_name">
              {shipping_first_name} {shipping_middle_name} {shipping_last_name}
            </p>
            <p>
              <span className="address_header">Email: </span> {shipping_email}
            </p>
            <p>
              <span className="address_header">Phone: </span>
              {shipping_phone}
            </p>
            <p>
              <span className="address_header">Company: </span>
              {shipping_company}
            </p>
            <p>
              <span className="address_header">Address: </span>
              {shipping_address_line_1} {shipping_address_line_2}
            </p>
            <p>
              <span className="address_header">City: </span>
              {shipping_city_name}
            </p>
            <p>
              <span className="address_header">State: </span>
              {shipping_state_name}
            </p>
            <p>
              <span className="address_header">Country: </span>
              {shipping_country_name}
            </p>
            <p>
              <span className="address_header">Landmark: </span>
              {shipping_landmark}
            </p>
            <p>
              <span className="address_header">Pincode: </span>
              {shipping_pincode}
            </p>
          </div>

          {/* billing address */}
          <div>
            <h4>Billing Address</h4>
            <p className="address_user_name">
              {first_name} {middle_name} {last_name}
            </p>
            <p>
              <span className="address_header">Email: </span>
              {email}
            </p>
            <p>
              <span className="address_header">Phone: </span>
              {phone}
            </p>
            <p>
              <span className="address_header">Company: </span>
              {company}
            </p>
            <p>
              <span className="address_header">Address: </span>
              {address_line_1} {address_line_2}
            </p>
            <p>
              <span className="address_header">City: </span>
              {city_name}
            </p>
            <p>
              <span className="address_header">State: </span>
              {state_name}
            </p>
            <p>
              <span className="address_header">Country: </span>
              {country_name}
            </p>
            <p>
              <span className="address_header">Landmark: </span>
              {landmark}
            </p>
            <p>
              <span className="address_header">Pincode: </span>
              {pincode}
            </p>
          </div>
        </div>
        <button
          className="delete_address_button"
          onClick={() => handleDeleteAddress(id)}
        >
          <RiDeleteBin6Fill />
        </button>
      </div>
    </>
  );
}
