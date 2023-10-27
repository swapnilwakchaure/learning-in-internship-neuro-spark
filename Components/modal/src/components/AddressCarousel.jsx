import React, { useState } from "react";
import { Carousel } from "react-bootstrap";
import { RiArrowLeftSLine, RiArrowRightSLine } from "react-icons/ri";

const AddressCarousel = ({ addresses }) => {
  const [index, setIndex] = useState(0);
  const itemsPerSlide = 1;

  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

  return (
    <Carousel
      activeIndex={index}
      onSelect={handleSelect}
      indicators={false}
      interval={null}
    >
      {addresses.map((address, addressIndex) => (
        <Carousel.Item key={addressIndex}>
          <div className="address-box"></div>
        </Carousel.Item>
      ))}
      <span
        aria-hidden="true"
        style={{
          border: "1px solid",
          borderRadius: "50%",
          color: "black",
        }}
        className="carousel-control-prev-icon"
        onClick={() =>
          handleSelect(
            (index - itemsPerSlide + addresses.length) % addresses.length
          )
        }
      >
        <RiArrowLeftSLine />
      </span>
      <span
        aria-hidden="true"
        style={{
          border: "1px solid",
          borderRadius: "50%",
          color: "black",
        }}
        className="carousel-control-next-icon"
        onClick={() => handleSelect((index + itemsPerSlide) % addresses.length)}
        // onClick={() => handleSelect(1)}
      >
        <RiArrowRightSLine />
      </span>
    </Carousel>
  );
};

export default AddressCarousel;
