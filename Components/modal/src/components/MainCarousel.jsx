import { Carousel } from "react-bootstrap";
import { useEffect, useState } from "react";
import "./main.css";

const MainCarousel = () => {
  // const [cardsPerSlide, setCardsPerSlide] = useState(4);

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

  useEffect(() => {
    const handleResize = () => {
      const screenWidth = window.innerWidth;

      if (screenWidth <= 320) {
        setCardsPerSlide(1);
      } else if (screenWidth >= 375 && screenWidth < 768) {
        setCardsPerSlide(2);
      } else if (screenWidth >= 768 && screenWidth <= 1024) {
        setCardsPerSlide(3);
      } else {
        setCardsPerSlide(4);
      }
    };

    window.addEventListener("resize", handleResize);

    handleResize();

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return (
    <>
      <div className="col-12 mt-2" id="leftDiv">
        <div className="address-carousel">
          <div className="saved-addresses ml-3 pt-3">
            <h3>
              <b>Previous Shipping Addresses</b>
            </h3>
          </div>

          <Carousel interval={null} wrap={false}>
            {addresses.map((chunkedKeys, slideIndex) => (
              <Carousel.Item key={`carousel-slide-${slideIndex}`}>
                <div className="d-flex justify-content-center p-5">
                  <strong>{chunkedKeys.name}</strong>
                  <p className="address-details">{chunkedKeys.address}</p>
                  <p className="address-details">{chunkedKeys.phone}</p>
                  <p className="address-details">
                    {chunkedKeys.state}
                    {chunkedKeys.pincode}
                  </p>
                </div>
              </Carousel.Item>
            ))}
          </Carousel>
        </div>
      </div>
    </>
  );
};

export default MainCarousel;
