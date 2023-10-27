import React, { useEffect, useState } from "react";
import { Carousel, Container, Row, Col } from "react-bootstrap";
import "./chat.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faChevronLeft,
  faChevronRight,
} from "@fortawesome/free-solid-svg-icons";
import "font-awesome/css/font-awesome.min.css";

const FirstCarousel = ({ addresses }) => {
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

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

    console.log("items: ", itemsPerSlide);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, [itemsPerSlide]);

  const prevAddress = () => {
    setIndex((index - 1 + addresses.length) % addresses.length);
  };

  const nextAddress = () => {
    setIndex((index + 1) % addresses.length);
  };

  return (
    <Container>
      <Carousel activeIndex={index} onSelect={handleSelect}>
        {addresses.map((address, idx) => (
          <Carousel.Item key={idx}>
            <Row className="justify-content-center">
              <Col lg={4} md={6} sm={12}>
                <div className="address-box">
                  <h3>Shipping Address</h3>
                  <h5>Name: {address.name}</h5>
                  <p>Phone: {address.phone}</p>
                  <p>Address: {address.address}</p>
                  <p>State: {address.state}</p>
                  <p>Pincode: {address.pincode}</p>
                </div>
              </Col>
            </Row>
            {/* <Carousel.Caption className="carousel-buttons">
              <p>
                <FontAwesomeIcon icon={faChevronLeft} onClick={prevAddress} />
              </p>
              <p>
                <FontAwesomeIcon icon={faChevronRight} onClick={nextAddress} />
              </p>
            </Carousel.Caption> */}
          </Carousel.Item>
        ))}
      </Carousel>
    </Container>
  );
};

export default FirstCarousel;
