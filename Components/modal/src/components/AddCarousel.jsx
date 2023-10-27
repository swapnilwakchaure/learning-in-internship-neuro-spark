import React, { useState } from "react";
import { Carousel } from "react-bootstrap";

const AddCarousel = ({ addresses }) => {
  const itemsPerSlide =
    window.innerWidth >= 992 ? 3 : window.innerWidth >= 768 ? 2 : 1;

  const totalSlides = Math.ceil(addresses.length / itemsPerSlide);

  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

  return (
    <Carousel activeIndex={index} onSelect={handleSelect} className="my-4">
      {Array.from({ length: totalSlides }).map((_, slideIndex) => {
        const startIdx = slideIndex * itemsPerSlide;
        const endIdx = startIdx + itemsPerSlide;
        const items = addresses.slice(startIdx, endIdx);

        return (
          <Carousel.Item key={slideIndex}>
            <div className="d-flex justify-content-between">
              {items.map((address, itemIndex) => (
                <div key={itemIndex} className="carousel-address-box">
                  {/* Render your address box component using the 'address' object */}
                  <h3>Shipping Address</h3>
                  <h5>{address.name}</h5>
                  <p>{address.phone}</p>
                  <p>{address.address}</p>
                  <p>{address.state}</p>
                  <p>{address.pincode}</p>
                </div>
              ))}
            </div>
          </Carousel.Item>
        );
      })}
    </Carousel>
  );
};

export default AddCarousel;