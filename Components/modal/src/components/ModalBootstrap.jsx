import { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";

const ModalBootstrap = () => {
  const [showModal, setShowModal] = useState(false);
  const [selectAddressType, setSelectAddressType] = useState("");
  const [chooseSaveType, setChooseSaveType] = useState("");

  const onSubmitModalForm = () => {
    if (selectAddressType && chooseSaveType) {
        const payload = { selectAddressType, chooseSaveType };
        console.log('payload: ',payload);
        setSelectAddressType("");
        setChooseSaveType("");
        setShowModal(false);
    } else {
        console.log('all fields are required');
    }
  };

  return (
    <>
      <Button variant="primary" onClick={() => setShowModal(true)}>
        Launch demo modal
      </Button>

      <Modal show={showModal} onHide={() => setShowModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Do you want to change address type</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form.Select
            aria-label="user needs to send action form"
            value={selectAddressType}
            onChange={(e) => setSelectAddressType(e.target.value)}
          >
            <option>Select Address Type </option>
            <option value="Home">Home</option>
            <option value="Office">Office</option>
          </Form.Select>
          <div onChange={(e) => setChooseSaveType(e.target.value)}>
            <Form.Check
              type="radio"
              id="updateAddress"
              name="addresstype"
              value={"updateAddress"}
              defaultChecked={chooseSaveType === "updateAddress"}
              custom
              label="Update Selected Address"
            />
            <Form.Check
              type="radio"
              id="addNewAddress"
              name="addresstype"
              value={"addNewAddress"}
              defaultChecked={chooseSaveType === "addNewAddress"}
              custom
              label="Add as a New Address"
            />
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="primary" onClick={onSubmitModalForm}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default ModalBootstrap;
