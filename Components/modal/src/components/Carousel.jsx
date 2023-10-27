import Carousel from "react-bootstrap/Carousel";

const CarouselComponent = () => {
  const data = [
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
  ];

  console.log(data);
  return (
    <Carousel data-bs-theme="dark" style={{ marginTop: "500px" }}>
      {data.length > 0 &&
        data.map((el) => {
          return (
            <Carousel.Item key={el.id}>
              {/* <img
                className="d-block w-50 m-auto"
                src="https://img.freepik.com/free-vector/dark-black-background-design-with-stripes_1017-38064.jpg"
                alt="cakes"
              /> */}
              <Carousel.Caption
                style={{ border: "3px solid red" }}
              >
                <h3>Shipping Address</h3>
                <h5>Name: {el.name}</h5>
                <p>Phone: {el.phone}</p>
                <p>Address: {el.address}</p>
                <p>State: {el.state}</p>
                <p>Pincode: {el.pincode}</p>
              </Carousel.Caption>
            </Carousel.Item>
          );
        })}
    </Carousel>
  );
};

export default CarouselComponent;
