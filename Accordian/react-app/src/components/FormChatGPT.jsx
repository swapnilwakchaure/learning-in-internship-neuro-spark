import React, { useState } from "react";
import { Accordion, Card, Button } from "react-bootstrap";

const FormChatGPT = () => {
  const [isForm1Open, setForm1Open] = useState(true);
  const [isForm2Open, setForm2Open] = useState(false);

  const toggleForms = () => {
    setForm1Open(!isForm1Open);
    setForm2Open(!isForm2Open);
  };

  return (
    <div>
      <Button onClick={toggleForms}>Toggle Forms</Button>
      <Accordion defaultActiveKey="0">
        <Card>
          <Accordion.Toggle
            as={Card.Header}
            eventKey="0"
            onClick={() => setForm1Open(!isForm1Open)}
          >
            Form 1
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="0" in={isForm1Open}>
            <Card.Body>{/* Form 1 Content */}</Card.Body>
          </Accordion.Collapse>
        </Card>
        <Card>
          <Accordion.Toggle
            as={Card.Header}
            eventKey="1"
            onClick={() => setForm2Open(!isForm2Open)}
          >
            Form 2
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="1" in={isForm2Open}>
            <Card.Body>{/* Form 2 Content */}</Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    </div>
  );
};

export default FormChatGPT;
