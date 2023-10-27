import { useState } from "react";
import Modal from "react-modal";

const customStyles = {
  content: {
    top: "11%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
  },
};

// Make sure to bind modal to your appElement (https://reactcommunity.org/react-modal/accessibility/)
// Modal.setAppElement('#yourAppElement');

const ModalHook = () => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectAddressType, setSelectAddressType] = useState("");
  const [chooseSaveType, setChooseSaveType] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (selectAddressType && chooseSaveType) {
      const payload = { selectAddressType, chooseSaveType };
      console.log(payload);
      setSelectAddressType("");
      setChooseSaveType("");
      setModalIsOpen(false);
    } else {
      console.log("all fields are required");
    }
  };

  return (
    <div
      style={{
        width: "100%",
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <button onClick={() => setModalIsOpen(true)}>Open Modal</button>

      <Modal
        isOpen={modalIsOpen}
        onRequestClose={() => setModalIsOpen(false)}
        style={customStyles}
        contentLabel="Example Modal"
      >
        <form onSubmit={handleSubmit}>
          <select
            style={{
                width: "100%"
            }}
            value={selectAddressType}
            onChange={(e) => setSelectAddressType(e.target.value)}
          >
            <option value="">Select Address Type</option>
            <option value="Home">Home</option>
            <option value="Office">Office</option>
          </select>
          <div onChange={(e) => setChooseSaveType(e.target.value)}>
            <input
              type="radio"
              name="addresstype"
              value={"updateAddress"}
              defaultChecked={chooseSaveType === "updateAddress"}
            />
            <label>Update Selected Address</label>
            <br />
            <input
              type="radio"
              name="addresstype"
              value={"addNewAddress"}
              defaultChecked={chooseSaveType === "addNewAddress"}
            />
            <label>Add as a New Address</label>
          </div>
          <button
            style={{
              margin: "10px 0px 0px 140px",
              background: "maroon",
              color: "white",
              border: "none",
              borderRadius: "5px",
              padding: "5px 10px"
            }}
          >
            OK
          </button>
        </form>
      </Modal>
    </div>
  );
};

export default ModalHook;
