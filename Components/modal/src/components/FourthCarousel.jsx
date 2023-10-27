import { useEffect, useRef } from "react";
import "./Styles/fourth.css";

const addresses = [
  {
    id: 1,
    name: "Ram Ambre",
    phone: "9876543210",
    address: "Ramnagar",
    state: "Maharashtra",
    pincode: "411008",
  },
  {
    id: 2,
    name: "Sham Ambre",
    phone: "9876542210",
    address: "Shamnagar",
    state: "Maharashtra",
    pincode: "411018",
  },
  {
    id: 3,
    name: "Radha Ambre",
    phone: "9872543210",
    address: "Radhanagar",
    state: "Maharashtra",
    pincode: "411108",
  },
  {
    id: 4,
    name: "Krishna Ambre",
    phone: "9876553210",
    address: "Krishnanagar",
    state: "Maharashtra",
    pincode: "411038",
  },
  {
    id: 5,
    name: "Ravan Ambre",
    phone: "9877543210",
    address: "Ravannagar",
    state: "Maharashtra",
    pincode: "413008",
  },
  {
    id: 6,
    name: "Dashanan Ambre",
    phone: "9876542210",
    address: "Dashanagar",
    state: "Maharashtra",
    pincode: "431008",
  },
  {
    id: 7,
    name: "Lakh Ambre",
    phone: "9872542210",
    address: "lakhanagar",
    state: "Maharashtra",
    pincode: "421008",
  },
];

const FourthCarousel = () => {
  const carouselRef = useRef(null);

  useEffect(() => {
    const width = carouselRef.current.clientWidth;
    console.log("width: ", width);
  });

  const handlePrevBtn = () => {
    // let width = box.clientWidth;
    const width = carouselRef.current.clientWidth;
    carouselRef.current = carouselRef.current - width;
    console.log(width);
  };

  const handleNextBtn = () => {
    // let width = box.clientWidth;
    const width = carouselRef.current.clientWidth;
    carouselRef.current = carouselRef.current + width;
    console.log(width);
  };

  return (
    <div>
      <h1>Carousel Component</h1>

      <div className="carousel-container">
        <div className="product-container" ref={carouselRef}>
          {addresses.length > 0 &&
            addresses.map((el) => (
              <div className="card-container" key={el.id}>
                <h3>{el.name}</h3>
                <p>Phone: {el.phone}</p>
                <p>Address: {el.address}</p>
                <p>State: {el.state}</p>
                <p>Pincode: {el.pincode}</p>
              </div>
            ))}
        </div>
        <button className="carousel-prev-btn" onClick={handlePrevBtn}>
          <p>&lt;</p>
        </button>
        <button className="carousel-next-btn" onClick={handleNextBtn}>
          <p>&gt;</p>
        </button>
      </div>
    </div>
  );
};

export default FourthCarousel;
