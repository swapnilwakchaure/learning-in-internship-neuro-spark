import "./App.css";
import FifthCarousel from "./components/FifthCarousel";
// import FourthCarousel from "./components/FourthCarousel";
// import ThirdCarousel from "./components/ThirdCarousel";
// import AddressCarousel from './components/MorningCarousel';
// import FixedCarousel from './components/FixedCarousel';
// import AddCarousel from './components/AddCarousel';
// import NewCarousel from './components/NewCarousel';
// import MainCarousel from './components/MainCarousel';
// import AddressCarousel from './components/AddressCarousel';
// import ChatCarousel from './components/ChatCarousel';
// import FirstCarousel from './components/FirstCarousel';
// import SecondCarousel from "./components/SecondCarousel";
// import CarouselComponent from './components/Carousel';
// import ModalBootstrap from './components/ModalBootstrap';
// import ModalHook from './components/ModalHook';
// import ModalComponent from './components/ModalComponent';

function App() {
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
  return (
    <div className="App">
      {/* <ModalComponent /> */}
      {/* <ModalHook /> */}
      {/* <ModalBootstrap /> */}
      {/* <CarouselComponent /> */}
      {/* <ChatCarousel addresses={addresses} /> */}
      {/* <AddressCarousel addresses={addresses} /> */}
      {/* <MainCarousel /> */}
      {/* <NewCarousel addresses={addresses} /> */}
      {/* <AddCarousel addresses={addresses} /> */}
      {/* <FixedCarousel /> */}
      {/* <AddressCarousel /> */}
      {/* <FirstCarousel addresses={addresses} /> */}
      {/* <SecondCarousel addresses={addresses} /> */}
      { /*<ThirdCarousel /> */ }
      {/* <FourthCarousel /> */}
      <FifthCarousel addresses={addresses} />
    </div>
  );
}

export default App;
