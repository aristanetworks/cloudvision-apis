import React from 'react';

interface VersionData {
  name: string;
  label: string;
}

interface DocVersionBannerWrapperProps {
  version?: VersionData;
  [key: string]: any;
}

export default function DocVersionBannerWrapper(props: DocVersionBannerWrapperProps): JSX.Element | null {
  return null;
}

