import React, { useEffect, useState } from 'react';
import { Carousel } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Styles/third.css';


const ThirdComponent = () => {
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

  const items = [
    { id: 1, content: 'Item 1' },
    { id: 2, content: 'Item 2' },
    { id: 3, content: 'Item 3' },
    { id: 4, content: 'Item 4' },
    { id: 5, content: 'Item 5' },
    { id: 6, content: 'Item 6' },
    { id: 7, content: 'Item 7' },
    { id: 8, content: 'Item 8' },
    { id: 9, content: 'Item 9' }
  ];

  const itemsPerPage = 3;

  const totalItems = items.length;
  const totalPages = Math.ceil(totalItems / itemsPerPage);

  const start = index * itemsPerPage;
  const end = start + itemsPerPage;

  console.log("index: ", index,"start: ", start,"end: ",end);

  const slider = items.slice(start,end).map((item) => {
    return (
        <Carousel.Item key={item.id}>
            {item.content}
        </Carousel.Item>
    )
  })

  useEffect(() => {
    let res = items.slice(start,end);
    console.log('res: ',res);
  }, [index]);

  return (
    <div className="carousel-container">
      <Carousel activeIndex={index} onSelect={handleSelect} indicators={true}>
        {/* {items.slice(start, end).map(item => (
          <Carousel.Item key={item.id}>
            {item.content}
            <div className="carousel-item-content">{item.content}</div>
          </Carousel.Item>
        ))} */}

        { slider}
      </Carousel>
      {/* <div className="carousel-buttons">
        <button className="carousel-button" onClick={() => setIndex(index > 0 ? index - 1 : totalPages - 1)}>
          Previous
        </button>
        <button className="carousel-button" onClick={() => setIndex(index < totalPages - 1 ? index + 1 : 0)}>
          Next
        </button>
      </div> */}
    </div>
  );
};

export default ThirdComponent;
