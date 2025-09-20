#!/bin/bash

echo "🚀 PressWire v2 Setup Script"
echo "============================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found!"
    echo "   Creating from template..."
    cp .env.example .env
    echo "   ⚠️  Please update .env with your API keys"
else
    echo "✅ .env file exists"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run the Supabase setup to get SQL commands:"
echo "   python3 setup_supabase.py"
echo ""
echo "3. Execute the SQL in your Supabase dashboard"
echo ""
echo "4. Test the connection:"
echo "   python3 test_supabase.py"
echo ""
echo "5. Start the application:"
echo "   python3 main.py"
echo ""
echo "The app will be available at http://localhost:8000"