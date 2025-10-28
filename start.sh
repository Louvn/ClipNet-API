#!/bin/bash
cd frontend/app

echo "ClipNet > Installing node_modules..."
npm install 

echo "ClipNet > Building Optimized Production React App..."
npm run build || exit

echo "ClipNet > Copying build into /backend/react-build..."
mkdir -p ../../backend/react-build
cp -r ./build/* ../../backend/react-build

cd ../..

echo "ClipNet > Installing Python Requirements..."
pip install -r ./backend/requirements.txt

echo "ClipNet > Starting FastAPI..."
uvicorn backend:app