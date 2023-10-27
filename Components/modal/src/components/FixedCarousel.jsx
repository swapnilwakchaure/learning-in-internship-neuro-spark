import React, { useState } from "react";
import { Carousel, Button, Row, Col } from "react-bootstrap";

const addresses = [
  {
    id: 1,
    name: "Ram",
    phone: "9876543210",
    address: "Ramnagar",
    state: "Maharashtra",
    pincode: "411008",
  },
  {
    id: 2,
    name: "Sham",
    phone: "9876542210",
    address: "Shamnagar",
    state: "Maharashtra",
    pincode: "411018",
  },
  {
    id: 3,
    name: "Radha",
    phone: "9872543210",
    address: "Radhanagar",
    state: "Maharashtra",
    pincode: "411108",
  },
  {
    id: 4,
    name: "Krishna",
    phone: "9876553210",
    address: "Krishnanagar",
    state: "Maharashtra",
    pincode: "411038",
  },
  {
    id: 5,
    name: "Ravan",
    phone: "9877543210",
    address: "Ravannagar",
    state: "Maharashtra",
    pincode: "413008",
  },
  {
    id: 6,
    name: "Dashanan",
    phone: "9876542210",
    address: "Dashanagar",
    state: "Maharashtra",
    pincode: "431008",
  },
  {
    id: 7,
    name: "Lakh",
    phone: "9872542210",
    address: "lakhanagar",
    state: "Maharashtra",
    pincode: "421008",
  },
];

const FixedCarousel = () => {
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

  const handleNext = () => {
    const nextIndex = index === addresses.length - 1 ? 0 : index + 1;
    setIndex(nextIndex);
  };

  const handlePrev = () => {
    const prevIndex = index === 0 ? addresses.length - 1 : index - 1;
    setIndex(prevIndex);
  };

  return (
    <Row className="carousel-row">
      <Col md={9}>
        <Carousel activeIndex={index} onSelect={handleSelect} interval={null}>
          {addresses.map((address, idx) => (
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
          ))}
        </Carousel>
      </Col>
      <Col md={3} className="carousel-controls">
        <Button
          variant="secondary"
          onClick={handlePrev}
          className="carousel-button"
        >
          Previous
        </Button>
        <Button
          variant="primary"
          onClick={handleNext}
          className="carousel-button"
        >
          Next
        </Button>
      </Col>
    </Row>
  );
};

export default FixedCarousel;
