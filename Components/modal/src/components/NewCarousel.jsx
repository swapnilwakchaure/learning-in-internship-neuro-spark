import React, { useState, useEffect } from "react";
import { Carousel, Button } from "react-bootstrap";

const AddressCarousel = ({ addresses }) => {
  const [index, setIndex] = useState(0);
  const [numVisibleItems, setNumVisibleItems] = useState(1);

  const handleSelect = (selectedIndex) => {
    setIndex(selectedIndex);
  };

  const handlePrev = () => {
    setIndex((prevIndex) =>
      prevIndex === 0 ? addresses.length - 1 : prevIndex - 1
    );
  };

  const handleNext = () => {
    setIndex((prevIndex) =>
      prevIndex === addresses.length - 1 ? 0 : prevIndex + 1
    );
  };

  useEffect(() => {
    const handleResize = () => {
      // Calculate the number of visible items based on screen width
      const newNumVisibleItems = window.innerWidth >= 992 ? 3 : 1;
      setNumVisibleItems(newNumVisibleItems);
    };

    // Initial calculation
    handleResize();

    // Event listener for window resize
    window.addEventListener("resize", handleResize);

    // Cleanup on component unmount
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []); // Empty dependency array ensures the effect runs only once after the initial render

  const items = addresses.map((address, idx) => (
    <Carousel.Item key={idx}>
      <div className="address-box">
        <h3>Shipping Address</h3>
        <h5>{address.name}</h5>
        <p>{address.phone}</p>
        <p>{address.address}</p>
        <p>{address.state}</p>
        <p>{address.pincode}</p>
      </div>
    </Carousel.Item>
  ));

  return (
    <div>
      <Carousel
        activeIndex={index}
        onSelect={handleSelect}
        interval={null}
        nextIcon={null}
        prevIcon={null}
        slide={false}
        indicators={false}
      >
        {items.slice(0, numVisibleItems)}
      </Carousel>
      <div className="d-flex justify-content-between mt-3">
        <Button variant="secondary" onClick={handlePrev}>
          Previous
        </Button>
        <Button variant="secondary" onClick={handleNext}>
          Next
        </Button>
      </div>
    </div>
  );
};

export default AddressCarousel;
