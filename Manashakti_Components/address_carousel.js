import React, { useEffect, useState } from "react";
import { Carousel } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";
import "./carousel.css";

const AddressCarousel = ({
  addresses,
  selectAddressId,
  handleSetFormFields,
  handleDeleteAddress,
}) => {
  const [windowSize, setWindowSize] = useState({
    width: window.innerWidth,
    height: window.innerHeight,
  });

  const itemsPerSlide =
    windowSize.width >= 1440
      ? 4
      : windowSize.width >= 1024
      ? 3
      : windowSize.width >= 768
      ? 2
      : 1;

  useEffect(() => {
    const handleResize = () => {
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  let singleBoxArray;

  if (selectAddressId) {
    singleBoxArray = addresses.filter((item) => item.id === selectAddressId);
  }

  return (
    <>
      <div className="carousel-component-header">
        <h3>Previous Shipping Addresses</h3>
      </div>

      {selectAddressId === null ? (
        windowSize.width >= 1440 && addresses.length <= 4 ? (
          <div className="d-flex justify-content-center">
            {addresses.map((el) => (
              <div className="carousel-item-wrapper" key={el.id}>
                <div className="address-box">
                  <h5>
                    {el.shipping_first_name} {el.shipping_last_name}
                  </h5>
                  <p>Phone: {el.shipping_phone}</p>
                  <p>Address: {el.shipping_address_line_1}</p>
                  <p>State: {el.shipping_state_name}</p>
                  <p>Pincode: {el.shipping_pincode}</p>
                </div>
                <div className="address-use-delete-box">
                  <button onClick={() => handleSetFormFields(el)}>Use</button>
                  <button onClick={() => handleDeleteAddress(el.id)}>
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : windowSize.width >= 1024 && addresses.length <= 3 ? (
          <div className="d-flex justify-content-center">
            {addresses.map((el) => (
              <div className="carousel-item-wrapper" key={el.id}>
                <div className="address-box">
                  <h5>
                    {el.shipping_first_name} {el.shipping_last_name}
                  </h5>
                  <p>Phone: {el.shipping_phone}</p>
                  <p>Address: {el.shipping_address_line_1}</p>
                  <p>State: {el.shipping_state_name}</p>
                  <p>Pincode: {el.shipping_pincode}</p>
                </div>
                <div className="address-use-delete-box">
                  <button onClick={() => handleSetFormFields(el)}>Use</button>
                  <button onClick={() => handleDeleteAddress(el.id)}>
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : windowSize.width >= 768 && addresses.length <= 2 ? (
          <div className="d-flex justify-content-center">
            {addresses.map((el) => (
              <div className="carousel-item-wrapper" key={el.id}>
                <div className="address-box">
                  <h5>
                    {el.shipping_first_name} {el.shipping_last_name}
                  </h5>
                  <p>Phone: {el.shipping_phone}</p>
                  <p>Address: {el.shipping_address_line_1}</p>
                  <p>State: {el.shipping_state_name}</p>
                  <p>Pincode: {el.shipping_pincode}</p>
                </div>
                <div className="address-use-delete-box">
                  <button onClick={() => handleSetFormFields(el)}>Use</button>
                  <button onClick={() => handleDeleteAddress(el.id)}>
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        ) : windowSize.width >= 320 && addresses.length <= 1 ? (
          <div className="carousel-item-wrapper m-auto">
            <h5>
              {singleBoxArray[0].shipping_first_name}{" "}
              {singleBoxArray[0].shipping_last_name}
            </h5>
            <p>Phone: {singleBoxArray[0].shipping_phone}</p>
            <p>Address: {singleBoxArray[0].shipping_address_line_1}</p>
            <p>State: {singleBoxArray[0].shipping_state_name}</p>
            <p>Pincode: {singleBoxArray[0].shipping_pincode}</p>
          </div>
        ) : (
          <>
            <Carousel className="mt-4" interval={null}>
              {[...Array(Math.ceil(addresses.length / itemsPerSlide))].map(
                (_, index) => (
                  <Carousel.Item key={index}>
                    <div className="d-flex justify-content-center">
                      {addresses
                        .slice(
                          index * itemsPerSlide,
                          (index + 1) * itemsPerSlide
                        )
                        .map((user, userIndex) => (
                          <div
                            key={userIndex}
                            className="carousel-item-wrapper"
                            onClick={() => handleSetFormFields(user)}
                          >
                            <div className="address-box">
                              <h5>
                                {user.shipping_first_name}{" "}
                                {user.shipping_last_name}
                              </h5>
                              <p><span className="address-header">Phone</span>: {user.shipping_phone}</p>
                              <p><span className="address-header">Address</span>: {user.shipping_address_line_1}</p>
                              <p><span className="address-header">State</span>: {user.shipping_state_name}</p>
                              <p><span className="address-header">Pincode</span>: {user.shipping_pincode}</p>
                            </div>

                            <button
                              onClick={() => handleDeleteAddress(user.id)}
                            >
                              <FontAwesomeIcon icon={faTrash} />
                            </button>
                          </div>
                        ))}
                    </div>
                  </Carousel.Item>
                )
              )}
            </Carousel>
          </>
        )
      ) : (
        <div className="carousel-item-wrapper m-auto">
          <h5>
            {singleBoxArray[0].shipping_first_name}{" "}
            {singleBoxArray[0].shipping_last_name}
          </h5>
          <p>Phone: {singleBoxArray[0].shipping_phone}</p>
          <p>Address: {singleBoxArray[0].shipping_address_line_1}</p>
          <p>State: {singleBoxArray[0].shipping_state_name}</p>
          <p>Pincode: {singleBoxArray[0].shipping_pincode}</p>
        </div>
      )}
    </>
  );
};

export default AddressCarousel;
