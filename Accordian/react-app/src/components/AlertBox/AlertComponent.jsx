import React, { useState } from "react";

const AlertComponent = ({ onClose }) => {
  const [selectedOption, setSelectedOption] = useState("Home");
  const [radioOption, setRadioOption] = useState("Update");

  const handleSelectChange = (e) => {
    setSelectedOption(e.target.value);
  };

  const handleRadioChange = (e) => {
    setRadioOption(e.target.value);
  };

  const handleOkClick = () => {
    onClose({ selectedOption, radioOption });
  };

  return (
    <div className="modal">
      <select value={selectedOption} onChange={handleSelectChange}>
        <option value="Home">Home</option>
        <option value="Office">Office</option>
      </select>
      <div>
        <label>
          <input
            type="radio"
            value="Update"
            checked={radioOption === "Update"}
            onChange={handleRadioChange}
          />
          Update
        </label>
        <label>
          <input
            type="radio"
            value="Add"
            checked={radioOption === "Add"}
            onChange={handleRadioChange}
          />
          Add
        </label>
      </div>
      <button onClick={handleOkClick}>Ok</button>
    </div>
  );
};

export default AlertComponent;
