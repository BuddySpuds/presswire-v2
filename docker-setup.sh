#!/bin/bash

echo "🐳 PressWire v2 Docker Setup"
echo "============================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed!"
    echo "   Please install Docker Desktop from: https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "❌ Docker is not running!"
    echo "   Please start Docker Desktop and try again."
    exit 1
fi

echo "✅ Docker is installed and running"

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo "   Creating from template..."
    cp .env.example .env
    echo "   ⚠️  Please update .env with your API keys before running the app"
    echo ""
    read -p "Press Enter to continue after updating .env file..."
else
    echo "✅ .env file exists"
fi

# Build and start containers
echo ""
echo "🔨 Building Docker containers..."
docker-compose build

echo ""
echo "🚀 Starting services..."
docker-compose up -d

# Wait for services to be ready
echo ""
echo "⏳ Waiting for services to start..."
sleep 5

# Check if services are running
echo ""
echo "📊 Checking service status..."

if docker-compose ps | grep -q "presswire-web.*Up"; then
    echo "✅ Web service is running"
else
    echo "❌ Web service failed to start"
fi

if docker-compose ps | grep -q "presswire-redis.*Up"; then
    echo "✅ Redis service is running"
else
    echo "❌ Redis service failed to start"
fi

# Display logs
echo ""
echo "📜 Recent logs:"
docker-compose logs --tail=20

echo ""
echo "================================"
echo "✅ Docker setup complete!"
echo "================================"
echo ""
echo "🌐 Application is running at: http://localhost:8000"
echo "📚 API Documentation: http://localhost:8000/api/docs"
echo ""
echo "📝 Useful Docker commands:"
echo "  View logs:           docker-compose logs -f"
echo "  Stop services:       docker-compose down"
echo "  Restart services:    docker-compose restart"
echo "  Shell into web:      docker-compose exec web bash"
echo "  Run tests:           docker-compose exec web pytest"
echo ""
echo "🗃️ Supabase Dashboard: https://supabase.com/dashboard/project/klwyvgraddjrawnbonnd"
echo ""
echo "Next steps:"
echo "1. Visit http://localhost:8000 to see the app"
echo "2. Add your AI API key to .env file if not done"
echo "3. Run database setup in Supabase dashboard (see setup_supabase.py)"