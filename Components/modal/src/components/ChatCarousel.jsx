import React, { useEffect, useState } from "react";
import { Carousel, Container, Row, Col } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faChevronLeft,
  faChevronRight,
} from "@fortawesome/free-solid-svg-icons";
import "font-awesome/css/font-awesome.min.css";
import "./chat.css";

const ChatCarousel = ({ addresses }) => {
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

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  const generateSlides = () => {
    const slides = [];
    for (let i = 0; i < addresses.length; i += itemsPerSlide) {
      slides.push(
        <Carousel.Item key={i}>
          <Container
            style={{
              display: "flex",
              justifyContent: "space-around",
              alignItems: "center",
              border: "2px solid blue",
            }}
          >
            <Row style={{ border: "2px solid red" }}>
              {addresses.slice(i, i + itemsPerSlide).map((address, index) => (
                <Col
                  key={index}
                  style={{
                    border: "1px solid",
                    margin: "0px 10px",
                    borderRadius: "5px",
                  }}
                >
                  <div className="address-box">
                    <h3>Shipping Address</h3>
                    <h5>Name: {address.name}</h5>
                    <p>Phone: {address.phone}</p>
                    <p>Address: {address.address}</p>
                    <p>State: {address.state}</p>
                    <p>Pincode: {address.pincode}</p>
                  </div>
                </Col>
              ))}

              <Carousel.Caption>
                {/* Carousel Buttons */}
                <div className="carousel-buttons">
                  <button
                    className="prev-button"
                    onClick={() =>
                      setIndex(
                        (index - 1 + addresses.length) % addresses.length
                      )
                    }
                  >
                    <FontAwesomeIcon icon={faChevronLeft} />
                  </button>
                  <button
                    className="next-button"
                    onClick={() => setIndex((index + 1) % addresses.length)}
                  >
                    <FontAwesomeIcon icon={faChevronRight} />
                  </button>
                </div>
              </Carousel.Caption>
            </Row>
          </Container>
        </Carousel.Item>
      );
    }
    return slides;
  };

  return (
    <Carousel
      style={{
        width: "100%",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
      onSelect={handleSelect}
      // prevIcon={
      //   <span aria-hidden="true" className="carousel-control-prev-icon">
      //     <FontAwesomeIcon icon={faChevronLeft} />
      //   </span>
      // }
      // nextIcon={
      //   <span aria-hidden="true" className="carousel-control-next-icon">
      //     <FontAwesomeIcon icon={faChevronRight} />
      //   </span>
      // }
    >
      {generateSlides()}
    </Carousel>
  );
};

export default ChatCarousel;
