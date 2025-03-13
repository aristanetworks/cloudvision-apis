import React from 'react';

interface ShowVersionProps {
  version: string;
}

const ShowVersion: React.FC<ShowVersionProps> = ({ version }) => {
  return (
    <div style={{ fontWeight: 'bold', color: '#27569b' }}>
      Version: {version}
    </div>
  );
};

export default ShowVersion;
