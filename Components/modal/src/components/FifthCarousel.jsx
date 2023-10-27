import React from "react";
import { Carousel } from "react-bootstrap";

const FifthCarousel = ({ addresses }) => {
  const itemsPerSlide = 3;

  return (
    <Carousel className="mt-4">
      {[...Array(Math.ceil(addresses.length / itemsPerSlide))].map(
        (_, index) => (
          <Carousel.Item key={index}>
            <div className="d-flex justify-content-between">
              {addresses
                .slice(index * itemsPerSlide, (index + 1) * itemsPerSlide)
                .map((user, userIndex) => (
                  <div key={userIndex} className="carousel-item-wrapper">
                    <h3>{user.name}</h3>
                    <p>Phone: {user.phone}</p>
                    <p>Address: {user.address}</p>
                    <p>State: {user.state}</p>
                    <p>Pincode: {user.pincode}</p>
                  </div>
                ))}
            </div>
          </Carousel.Item>
        )
      )}
    </Carousel>
  );
};

export default FifthCarousel;
