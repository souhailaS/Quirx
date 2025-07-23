"""
LLM execution runner for generating responses to prompts

@author: souhailaS
"""

import os
import time
from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from abc import ABC, abstractmethod

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


@dataclass
class LLMResponse:
    text: str
    model: str
    tokens_used: int
    response_time: float
    error: Optional[str] = None


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    @abstractmethod
    def generate_response(self, prompt: str, **kwargs) -> LLMResponse:
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI API provider"""
    
    def __init__(self, api_key: str = None):
        if not OPENAI_AVAILABLE:
            raise ImportError("OpenAI package not installed. Install with: pip install openai")
        
        self.client = openai.OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
    
    def generate_response(self, prompt: str, model: str = "gpt-3.5-turbo", **kwargs) -> LLMResponse:
        start_time = time.time()
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=kwargs.get('max_tokens', 1000),
                temperature=kwargs.get('temperature', 0.7)
            )
            
            response_time = time.time() - start_time
            
            return LLMResponse(
                text=response.choices[0].message.content,
                model=model,
                tokens_used=response.usage.total_tokens,
                response_time=response_time
            )
            
        except Exception as e:
            return LLMResponse(
                text="",
                model=model,
                tokens_used=0,
                response_time=time.time() - start_time,
                error=str(e)
            )


class AnthropicProvider(LLMProvider):
    """Anthropic Claude API provider"""
    
    def __init__(self, api_key: str = None):
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("Anthropic package not installed. Install with: pip install anthropic")
        
        self.client = anthropic.Anthropic(api_key=api_key or os.getenv('ANTHROPIC_API_KEY'))
    
    def generate_response(self, prompt: str, model: str = "claude-3-5-sonnet-20241022", **kwargs) -> LLMResponse:
        start_time = time.time()
        
        try:
            response = self.client.messages.create(
                model=model,
                max_tokens=kwargs.get('max_tokens', 1000),
                messages=[{"role": "user", "content": prompt}]
            )
            
            response_time = time.time() - start_time
            
            return LLMResponse(
                text=response.content[0].text,
                model=model,
                tokens_used=response.usage.input_tokens + response.usage.output_tokens,
                response_time=response_time
            )
            
        except Exception as e:
            return LLMResponse(
                text="",
                model=model,
                tokens_used=0,
                response_time=time.time() - start_time,
                error=str(e)
            )


class MockProvider(LLMProvider):
    """Mock provider for testing without API calls"""
    
    def __init__(self, responses: List[str] = None):
        self.responses = responses or ["This is a mock response."]
        self.call_count = 0
    
    def generate_response(self, prompt: str, model: str = "mock-model", **kwargs) -> LLMResponse:
        start_time = time.time()
        time.sleep(0.1)  # Simulate API delay
        
        response_text = self.responses[self.call_count % len(self.responses)]
        self.call_count += 1
        
        return LLMResponse(
            text=response_text,
            model=model,
            tokens_used=len(prompt.split()) + len(response_text.split()),
            response_time=time.time() - start_time
        )


class LLMRunner:
    """Main runner class for executing LLM queries"""
    
    def __init__(self, provider: str = "openai", api_key: str = None, **kwargs):
        self.provider_name = provider
        
        if provider == "openai":
            if not OPENAI_AVAILABLE:
                raise ImportError("OpenAI package not installed. Install with: pip install openai")
            self.provider = OpenAIProvider(api_key)
        elif provider == "anthropic":
            if not ANTHROPIC_AVAILABLE:
                raise ImportError("Anthropic package not installed. Install with: pip install anthropic")
            self.provider = AnthropicProvider(api_key)
        elif provider == "mock":
            self.provider = MockProvider(kwargs.get('mock_responses'))
        else:
            raise ValueError(f"Unsupported provider: {provider}")
    
    def run_prompt(self, prompt: str, model: str = None, **kwargs) -> LLMResponse:
        """Execute a single prompt"""
        if model is None:
            model = self._get_default_model()
        
        return self.provider.generate_response(prompt, model=model, **kwargs)
    
    def run_batch(self, prompts: List[str], model: str = None, **kwargs) -> List[LLMResponse]:
        """Execute multiple prompts"""
        responses = []
        for prompt in prompts:
            response = self.run_prompt(prompt, model, **kwargs)
            responses.append(response)
            
            # Rate limiting - simple delay between requests
            if kwargs.get('rate_limit_delay', 0) > 0:
                time.sleep(kwargs['rate_limit_delay'])
        
        return responses
    
    def _get_default_model(self) -> str:
        """Get default model for the provider"""
        defaults = {
            "openai": "gpt-3.5-turbo",
            "anthropic": "claude-3-5-sonnet-20241022",
            "mock": "mock-model"
        }
        return defaults.get(self.provider_name, "gpt-3.5-turbo")
    
    def test_connection(self) -> bool:
        """Test if the LLM provider is accessible"""
        try:
            response = self.run_prompt("Hello", max_tokens=10)
            return response.error is None
        except Exception:
            return False 