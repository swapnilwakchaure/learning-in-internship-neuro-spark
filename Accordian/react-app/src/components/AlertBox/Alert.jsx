import AlertComponent from "./AlertComponent";

const Alert = () => {
  const handleShowAlert = () => {
    console.log("show alert");
  };

  return (
    <div>
      <h1>Alert Component</h1>
      <button onClick={() => handleShowAlert()}>ShowAlert</button>

      <AlertComponent onClose={handleShowAlert} />
    </div>
  );
};

export default Alert;
