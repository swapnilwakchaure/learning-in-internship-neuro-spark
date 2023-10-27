import React, { useState } from "react";
import { Carousel, Container, Row, Col } from "react-bootstrap";
import "./second.css";

const SecondCarousel = ({ addresses }) => {
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex) => {
    setIndex(selectedIndex);
  };

  return (
    <Container>
      <Row className="justify-content-center">
        <Col xs={12} sm={6} md={4} lg={4} xl={4}>
          <Carousel activeIndex={index} onSelect={handleSelect} interval={null}>
            {addresses.map((address, idx) => (
              <Carousel.Item key={idx}>
                <div className="address-box">
                  <h3>Shipping Address</h3>
                  <h5>Name: {address.name}</h5>
                  <p>Phone: {address.phone}</p>
                  <p>Address: {address.address}</p>
                  <p>State: {address.state}</p>
                  <p>Pincode: {address.pincode}</p>
                </div>
                <Carousel.Caption>
                  {/* Left Control */}
                  {idx > 0 && (
                    <span
                      className="carousel-control-prev"
                      onClick={() => handleSelect(idx - 1)}
                    >
                      &lt;
                    </span>
                  )}
                  {/* Right Control */}
                  {idx < addresses.length - 1 && (
                    <span
                      className="carousel-control-next"
                      onClick={() => handleSelect(idx + 1)}
                    >
                      &gt;
                    </span>
                  )}
                </Carousel.Caption>
              </Carousel.Item>
            ))}
          </Carousel>
        </Col>
      </Row>
    </Container>
  );
};

export default SecondCarousel;
