import { useState } from "react";
import "./modal.css";

const ModalComponent = () => {
  const [isSaveAddress, setIsSaveAddress] = useState("");
  const [saveType, setSaveType] = useState("");
  const [showModal, setShowModal] = useState(false);

  const addOrUpdateAddress = (e) => {
    e.preventDefault();

    if (saveType && isSaveAddress) {
      const payload = { saveType, isSaveAddress };
      console.log("payload: ", payload);
      setIsSaveAddress("");
      setSaveType("");
      setShowModal(false);
    }
  };

  return (
    <div className="modal-button-div">
      <button disabled={showModal} onClick={() => setShowModal(!showModal)}>
        Open Modal
      </button>

      {showModal && (
        <form className="modal-form" onSubmit={addOrUpdateAddress}>
          <p>Choose your address save option</p>
          <select
            value={saveType}
            onChange={(e) => setSaveType(e.target.value)}
          >
            <option value="">Select Address Type</option>
            <option value="Home">Home</option>
            <option value="Office">Office</option>
          </select>
          {!saveType && (
            <p className="address-error-message">select the address type</p>
          )}
          <div onChange={(e) => setIsSaveAddress(e.target.value)}>
            <input
              type="radio"
              name="addresstype"
              value={"updateAddress"}
              defaultChecked={isSaveAddress === "updateAddress"}
            />
            <label>Update Selected Address</label>
            <br />
            <input
              type="radio"
              name="addresstype"
              value={"addNewAddress"}
              defaultChecked={isSaveAddress === "addNewAddress"}
            />
            <label>Add as a New Address</label>
          </div>
          {!isSaveAddress && (
            <p className="address-error-message">choose the address change</p>
          )}
          <button>OK</button>
        </form>
      )}
      
    </div>
  );
};

export default ModalComponent;
